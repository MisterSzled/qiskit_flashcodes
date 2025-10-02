# 1.0.0 SparsePauliOp Basics
# Demonstrates how to create SparsePauliOp objects using from_sparse_list.

import numpy as np
from qiskit.quantum_info.operators import SparsePauliOp

# Create a SparsePauliOp from a list of triplets:
# Each triplet is (pauli_string, qubit_indices, coefficient)
#   pauli_string   -> defines the Pauli operators
#   qubit_indices  -> where the string acts (which qubits)
#   coefficient    -> scalar weight (real or complex)
op1 = SparsePauliOp.from_sparse_list(
        [("ZX", [1, 4], 1.0), ("YY", [0, 3], -1 + 1j)], num_qubits=5
)

print("SparsePauliOp op1 created:")
print(op1)  # Prints operator in compressed Pauli form

"""
SUMMARY:
- Demonstrates SparsePauliOp creation with from_sparse_list.
- Steps:
        1. Import SparsePauliOp.
        2. Define list of Pauli string terms with indices and coefficients.
        3. Call from_sparse_list with total number of qubits.
        4. Print resulting operator in human-readable form.
"""