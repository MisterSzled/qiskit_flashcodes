# 5.3.0 PUB Basics
# Demonstrates the Primitive Unified Block (PUB) structure.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli

# --- Step 1: Build a circuit ---
qc = QuantumCircuit(1)
qc.h(0)

# --- Step 2: Define an observable ---
obs = Pauli("Z")

# --- Step 3: PUBs are just standardized inputs ---
# Sampler PUB = [list of circuits]
pub_sampler = [qc]

# Estimator PUB = [(circuit, observable)]
pub_estimator = [(qc, obs)]

print("Sampler PUB:", pub_sampler)
print("Estimator PUB:", pub_estimator)

"""
SUMMARY:
        - PUB = Primitive Unified Block → standardized input format for primitives.
        - Sampler PUB: [circuits]
        - Estimator PUB: [(circuit, observable)]
        - PUBs are just lists/tuples, ensuring a consistent API for SamplerV2/EstimatorV2.
        - In Qiskit 2.x+, use SamplerV2 and EstimatorV2 from `qiskit_ibm_runtime`.
"""
