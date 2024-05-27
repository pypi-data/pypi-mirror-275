# Copyright 2024 Davide Gessa

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import pickle
import random
import time
import traceback

from requests.exceptions import ReadTimeout

from .blockchain import IPFSGateway, NearBlockchain, repeat_until_done
from .cli import default_parser
from .q import Circuit
from .utils import create_dqpu_dirs
from .verifier import BasicTrapper  # BasicTrapInfo,


def handle_pending_validation_job(j, ipfs, nb, base_dir):
    print(f"Processing pending-validation job {j['id']} from {j['owner_id']}")

    try:
        jf = ipfs.get(j["job_file"], timeout=10)
    except ReadTimeout:  # TODO: move on ipfs.get raising a new exception
        print(f"\tTimeout getting file {j['job_file']}, skipping for now")
        return False

    # Parse the file using q.Circuit.fromQasm
    try:
        qc = Circuit.fromQasmCircuit(jf.decode("ascii"))
    except Exception as e:
        print("\t", "Failed to parse", j["id"], e)
        nb.set_job_validity(j["id"], False)
        return True

    # Add a trap
    trapper = BasicTrapper()
    (qc2, trap_list) = trapper.trap(qc)

    # Save trap info to a file
    with open(f"{base_dir}/{j['id']}_qc_traps.pickle", "wb") as outp:
        pickle.dump(trap_list, outp, pickle.HIGHEST_PROTOCOL)

    # Save qasm to file
    trapped_qasm_file = f"{base_dir}/{j['id']}_qc_trapped.qasm"

    with open(trapped_qasm_file, "w") as f:
        f.write(qc2.toQasmCircuit())

    # Upload the file
    jf_trapped = ipfs.upload(trapped_qasm_file)
    print("\tTrapped file uploaded", jf_trapped)

    # Send the set_validity
    print("\t", nb.set_job_validity(j["id"], True, jf_trapped))
    return True


def handle_validating_result_job(j, ipfs, nb, base_dir):  # noqa: C901
    print(
        f"Processing validating-result job {j['id']} from {j['owner_id']} "
        + f"sampled by {j['sampler_id']}"
    )

    # Get the result data
    try:
        rf = ipfs.get(j["result_file"], timeout=10)
    except ReadTimeout:  # TODO: move on ipfs.get raising a new exception
        print(f"\tTimeout getting file {j['result_file']}, skipping for now")
        return False

    try:
        counts = json.loads(rf)
    except:
        print("\tInvalid result data")
        print(nb.set_result_validity(j["id"], False))
        return True

    # Check if shots match
    ctot = sum(counts.values())
    if j["shots"] > ctot:
        print("\t", "Invalid number of shots")
        print(nb.set_result_validity(j["id"], False))
        return True

    # Load the trap from file
    trap_fp = f"{base_dir}/{j['id']}_qc_traps.pickle"
    try:
        with open(trap_fp, "rb") as inp:
            trap_list = pickle.load(inp)
    except:
        print(f'Unable to load {trap_fp}, skipping job {j["id"]}')
        return False

    # Check trap validity
    try:
        trapper = BasicTrapper()
        validity = trapper.verify(trap_list, counts)
    except Exception as e:
        print("Got exception while verifying, contact dakk")
        print(e)
        return False

    # Send the set_result_validity
    if validity:
        trap_j = list(map(lambda t: t.dump(), trap_list))
        trap_file = f"{base_dir}/{j['id']}_traps.json"

        with open(trap_file, "w") as inp:
            inp.write(json.dumps(trap_j))

        trap_file_i = ipfs.upload(trap_file)

        print("\t", nb.set_result_validity(j["id"], True, trap_file_i))
    else:
        print("\t", nb.set_result_validity(j["id"], False))

    return True


def verifier_node():  # noqa: C901
    parser = default_parser()
    args = parser.parse_args()  # noqa: F841

    base_dir = create_dqpu_dirs()

    nb = NearBlockchain(args.account, args.network)
    ipfs = IPFSGateway(gateway="http://" + args.ipfs_gateway)  # noqa: F841

    # Start contract polling for new jobs
    running = True
    first_run = True
    n_vresult = 0
    n_verified = 0

    print("Verifier node started.")
    stats = repeat_until_done(lambda: nb.get_jobs_stats())

    while running:
        if first_run:
            first_run = False
            latest_jobs = repeat_until_done(lambda: nb.get_all_jobs())
        else:
            i = 0
            while (
                repeat_until_done(lambda: nb.get_jobs_stats())["validating-result"]
                == stats["validating-result"]
                and repeat_until_done(lambda: nb.get_jobs_stats())["pending-validation"]
                == stats["pending-validation"]
            ) and i < 5:
                time.sleep(random.randint(0, 5))
                i += 1

            latest_jobs = repeat_until_done(lambda: nb.get_latest_jobs())

        stats = repeat_until_done(lambda: nb.get_jobs_stats())
        random.shuffle(latest_jobs)

        # If there is a new job that needs validation, process it
        for j in latest_jobs:
            if j["status"] == "pending-validation":
                try:
                    if handle_pending_validation_job(j, ipfs, nb, base_dir):
                        n_verified += 1
                        stats["pending-validation"] -= 1
                except Exception as e:
                    print("\tFailed to handle pending-validation job:", e)
                    traceback.print_exc()

            elif (
                j["status"] == "validating-result"
                and j["verifier_id"] == nb.account.account_id
            ):
                try:
                    if handle_validating_result_job(j, ipfs, nb, base_dir):
                        n_vresult += 1
                        stats["validating-result"] -= 1
                except Exception as e:
                    print("\tFailed to handle validating-result job:", e)
                    traceback.print_exc()

        print(
            f"Account balance is {nb.balance():0.5f} N, job verified {n_verified}, "
            + f"result verified {n_vresult}"
        )
