# Demonstrating linear combinations of Operators.

from qiskit.quantum_info import Operator, Pauli

XX = Operator(Pauli("XX"))
YY = Operator(Pauli("YY"))
ZZ = Operator(Pauli("ZZ"))

# Combine with scalar coefficients
op = 0.5 * (XX + YY - 3 * ZZ)
print("Linear combination result:\n", op.data, "\n")

# Check unitarity
print("Is the resulting operator unitary?", op.is_unitary())

"""
SUMMARY:
- Demonstrates linear combinations of Operators.
- Steps:
        1. Create Operators for XX, YY, ZZ.
        2. Form a linear combination with scalars.
        3. Show that result may be non-unitary.
"""
