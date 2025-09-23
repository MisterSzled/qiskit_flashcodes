# Demonstrating operator composition (matrix multiplication).

from qiskit.quantum_info import Operator, Pauli
import numpy as np

A = Operator(Pauli("X"))  # Pauli-X
B = Operator(Pauli("Z"))  # Pauli-Z

# Default composition: A.compose(B) = B * A
comp = A.compose(B)
print("Compose A ∘ B (B after A):\n", comp.data, "\n")

# Front=True: apply B first, then A => A * B
comp_front = A.compose(B, front=True)
print("Compose with front=True (A after B):\n", comp_front.data, "\n")

# Subsystem composition
op3 = Operator(np.eye(2**3))   # 3-qubit identity operator
xz = Operator(Pauli("XZ"))     # 2-qubit operator
sub_comp = op3.compose(xz, qargs=[0, 2])  # place on qubits 0 and 2
print("Subsystem composition (XZ on qubits 0,2 of 3-qubit op):\n", sub_comp.data)

"""
SUMMARY:
- Demonstrates composition of operators.
- Steps:
        1. Show basic composition (matrix multiply).
        2. Show reversed composition with front=True.
        3. Place smaller operator into specific subsystems with qargs.
"""
