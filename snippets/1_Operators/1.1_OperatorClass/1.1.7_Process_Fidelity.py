# Demonstrating process fidelity comparison of Operators.

import numpy as np
from qiskit.quantum_info import Operator, process_fidelity
from qiskit.circuit.library import XGate

# Define two operators differing by a global phase
op_a = Operator(XGate())
op_b = np.exp(1j * 0.5) * Operator(XGate())

# Compute process fidelity
F = process_fidelity(op_a, op_b)
print("Process fidelity =", F)

"""
SUMMARY:
- Shows use of process_fidelity() to compare Operators.
- Steps:
        1. Create two operators (one is a phase-shifted version of the other).
        2. Compute process fidelity → returns 1.0 (phase-independent).
        3. Demonstrates fidelity as a robust measure of closeness.
"""
