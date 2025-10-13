# 1.0.1 SparsePauliOp Arithmetic
# Demonstrates supported arithmetic operations on SparsePauliOp objects.

from qiskit.quantum_info.operators import SparsePauliOp

# Define two operators with different Pauli terms
op1 = SparsePauliOp.from_sparse_list(
        [("ZX", [1, 4], 1.0), ("YY", [0, 3], -1 + 1j)], num_qubits=5
)
op2 = SparsePauliOp.from_sparse_list(
        [("XXZ", [0, 1, 4], 1 + 2j), ("ZZ", [1, 2], -1 + 1j)], num_qubits=5
)

# Addition of operators
print("op1 + op2:")
print(op1 + op2)
print()

# Multiplication by a scalar
print("2 * op1:")
print(2 * op1)
print()

# Operator multiplication (composition, matrix product form)
print("op1 @ op2:")
print(op1 @ op2)
print()

# Tensor product (Kronecker product)
print("op1.tensor(op2):")
print(op1.tensor(op2))

"""
SUMMARY:
- Demonstrates arithmetic with SparsePauliOp.
- Steps:
        1. Create op1 and op2 via from_sparse_list.
        2. Perform operator addition.
        3. Multiply op1 by scalar (2).
        4. Perform operator composition using @.
        5. Compute tensor product of op1 and op2.
"""
