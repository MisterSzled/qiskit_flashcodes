# 5.3.1 PUB with Parameters
# Demonstrates PUB structure including parameter bindings.

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.quantum_info import Pauli
import numpy as np

# --- Step 1: Parametrized circuit ---
theta = Parameter("θ")
qc = QuantumCircuit(1)
qc.ry(theta, 0)

# --- Step 2: Observable ---
obs = Pauli("Z")

# --- Step 3: PUB with parameter binding
# Format: (circuit, observable, [param_values])
param_value = [np.pi / 2]
pub = [(qc, obs, param_value)]

print("PUB with parameters:", pub)

"""
SUMMARY:
        - PUBs can include parameter bindings:
                [(circuit, observable, [param_values])]
        - This allows reusing the same parametrized circuit with different inputs.
        - Core to EstimatorV2 workflows in `qiskit_ibm_runtime`.
        - Note: Old `Estimator` primitive was removed in Qiskit 2.x.
"""
