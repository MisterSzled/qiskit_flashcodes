# Demonstrating comparison of Operators.

import numpy as np
from qiskit.quantum_info import Operator, Pauli
from qiskit.circuit.library import XGate

# Equality check
eq_check = (Operator(Pauli("X")) == Operator(XGate()))
print("Operator(Pauli('X')) == Operator(XGate()):", eq_check)

# Equality fails with global phase difference
phase_diff = (Operator(XGate()) == np.exp(1j * 0.5) * Operator(XGate()))
print("With global phase factor:", phase_diff)

"""
SUMMARY:
- Shows equality comparison of Operators.
- Steps:
        1. Compare Operator(Pauli("X")) and Operator(XGate()) → True.
        2. Apply global phase and check again → False (phase not ignored).
"""
