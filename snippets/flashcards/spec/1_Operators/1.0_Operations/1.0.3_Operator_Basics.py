# 1.0.3 Operator Basics
# Demonstrates Operator class for dense matrix representation.

import numpy as np
from qiskit.quantum_info.operators import Operator

# Define a 2-qubit XX operator as a dense numpy array
XX = Operator(
    np.array(
        [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
        ]
    )
)

print("Operator XX created:")
print(XX)  # Prints operator matrix with input/output dims
print()

# Access underlying data
print("Underlying numpy array (Operator.data):")
print(XX.data)
print()

# Access dimensions
input_dim, output_dim = XX.dim
print("Input dimension:", input_dim)
print("Output dimension:", output_dim)

"""
SUMMARY:
- Demonstrates Operator class with explicit dense matrix input.
- Steps:
        1. Import Operator.
        2. Build numpy array for Pauli XX operator.
        3. Initialize Operator with this array.
        4. Print operator object with metadata.
        5. Access underlying data array.
        6. Access and print input/output dimensions.
"""
