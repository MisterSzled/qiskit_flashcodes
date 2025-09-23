# 1.0.2 Pauli Basics
# Demonstrates Pauli class usage with phases and matrix representation.

import numpy as np
from qiskit.quantum_info.operators import Pauli

# Initialize Pauli operator with "iXX"
#   "XX" means Pauli X ⊗ X
#   "i" prefix introduces a phase factor of i
op1 = Pauli("iXX")

print("Pauli operator op1:")
print(op1)
print()

# Inspect properties
print(f"Dimension of {op1}: {op1.dim}")  # (4,4) since 2-qubit operator
print(f"Phase of {op1}: {op1.phase}")    # Encoded as an integer 0–3
print("Matrix representation:")
print(op1.to_matrix())

"""
SUMMARY:
- Demonstrates Pauli class creation and inspection.
- Steps:
        1. Initialize Pauli with string (including optional phase prefix).
        2. Print operator object.
        3. Get and print operator dimension.
        4. Get and print phase.
        5. Convert operator to matrix and display.
"""
