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

from qiskit import qasm2, transpile
from qiskit_aer import AerSimulator

from .sampler import Sampler


class AerSimulatorSampler(Sampler):
    def sample(self, shots):
        qc = qasm2.loads(
            self.circuit, custom_instructions=qasm2.LEGACY_CUSTOM_INSTRUCTIONS
        )  # .toQasmCircuit())
        simulator = AerSimulator()
        circ = transpile(qc, simulator)
        result = simulator.run(circ, shots=shots).result()
        counts = result.get_counts(circ)
        return counts
