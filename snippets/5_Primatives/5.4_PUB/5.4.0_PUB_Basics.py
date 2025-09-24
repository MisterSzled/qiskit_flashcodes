# 5.4.0 PUB Basics
# Demonstrates the Primitive Unified Block (PUB) structure.

from qiskit.primitives import Sampler, Estimator
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import Pauli

# Build a circuit
qc = QuantumCircuit(1)
qc.h(0)

# Observable for Estimator
obs = Pauli("Z")

# PUB for Sampler → just a list of circuits
pub_sampler = [qc]

# PUB for Estimator → list of (circuit, observable) tuples
pub_estimator = [(qc, obs)]

print("Sampler PUB:", pub_sampler)
print("Estimator PUB:", pub_estimator)

"""
SUMMARY:
        - PUB = Primitive Unified Block → standardized input format for primitives.
        - Sampler PUB: [circuits]
        - Estimator PUB: [(circuit, observable)]
        - Ensures consistent, predictable input API.
"""
