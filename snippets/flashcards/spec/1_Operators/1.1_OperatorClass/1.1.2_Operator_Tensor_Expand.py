# Demonstrating tensor product and expansion of Operators.

from qiskit.quantum_info import Operator, Pauli

A = Operator(Pauli("X"))  # Pauli-X operator
B = Operator(Pauli("Z"))  # Pauli-Z operator

# Tensor product: A ⊗ B (Z acts on qubit 0, X on qubit 1)
tensor_ab = A.tensor(B)
print("Tensor product (A ⊗ B):\n", tensor_ab.data, "\n")

# Expansion: B ⊗ A (order reversed)
expand_ab = A.expand(B)
print("Expansion (B ⊗ A):\n", expand_ab.data, "\n")

"""
SUMMARY:
        - Shows difference between tensor() and expand():
                * tensor: places right-hand operator on lower subsystem (A ⊗ B).
                * expand: reverses order (B ⊗ A).
        - Both combine single-qubit operators into 2-qubit systems.
"""
