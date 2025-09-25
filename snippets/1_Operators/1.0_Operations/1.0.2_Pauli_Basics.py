# 1.0.2 Pauli Basics
# Demonstrates Pauli class usage with phases and matrix representation.

# Notes
#       .phase is not a "look up in this ordered list of phases {1, i, -1, -i}"
#       it is actually 'what is the exponent of (-i)^phase_index in the ordered map above
#       .phase = 0 => (-i)^0 = +1
#       .phase = 1 => (-i)^1 = -i
#       .phase = 2 => (-i)^2 = -1
#       .phase = 3 => (-i)^3 = +i

#       This comes from quantum error correction:
#            Pauli multiplication is then just XOR on bit-vectors 
#            plus modular addition of the (−i)-phase exponent.

import numpy as np
from qiskit.quantum_info.operators import Pauli

# Initialize Pauli operator with "iXX"
#   "XX" means Pauli X ⊗ X
#   "i" prefix introduces a phase factor of i
op1 = Pauli("iXX")
op2 = Pauli("-iXX")

print("Pauli operator op1:")
print(op1)
print()
print("Pauli operator op2:")
print(op2)
print()

# Inspect properties
print(f"Dimension of {op1}: {op1.dim}")  # (4,4) since 2-qubit operator
print(f"Phase of {op1}: {op1.phase} aka (-i)^phase_index")    # Encoded as an integer 0–3
print("Matrix representation:")
print(op1.to_matrix())
print()

# Inspect properties
print(f"Dimension of {op2}: {op2.dim}")  # (4,4) since 2-qubit operator
print(f"Phase of {op2}: {op2.phase} aka (-i)^phase_index")    # Encoded as an integer 0–3
print("Matrix representation:")
print(op2.to_matrix())
print()

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
