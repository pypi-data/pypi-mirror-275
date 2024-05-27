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


class Sampler:
    """Abstract class that should be implemented by any sampler"""

    def __init__(self, circuit):
        if type(circuit) is not str:
            self.circuit = circuit.decode("ascii")
        else:
            self.circuit = circuit

    @classmethod
    def test(cls) -> bool:
        qc = (
            "OPENQASM 2.0;\n"
            'include "qelib1.inc";\n'
            "qreg q[2];\n"
            "creg c[2];\n"
            "h q[0];\n"
            "cx q[0], q[1];\n"
            "measure q -> c;"
        )
        c = cls(qc)
        r = c.sample(1024)

        if sorted(r.keys()) != ["00", "11"]:
            return False

        if (r["00"] + r["11"]) != 1024:
            return False

        return True

    def sample(self, shots):
        raise Exception("Not implemented")

    def compute(self):
        """Compute the statevector"""
        raise Exception("Not implemented")
