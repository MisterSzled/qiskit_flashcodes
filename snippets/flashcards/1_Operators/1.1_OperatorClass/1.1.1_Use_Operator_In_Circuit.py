# Demonstrating how to insert an Operator into a QuantumCircuit.

from qiskit.quantum_info import Operator, Pauli
from qiskit.circuit import QuantumCircuit

# Create an Operator from Pauli "XX"
xx_op = Operator(Pauli("XX"))
print("Operator is unitary?", xx_op.is_unitary())

# Add Operator to a circuit as a UnitaryGate
circ = QuantumCircuit(2, 2)
circ.append(xx_op, [0, 1])  # append operator on qubits 0 and 1
circ.measure([0, 1], [0, 1])
print("Circuit with Operator:\n", circ)

# Directly append Pauli (auto-converted to gates)
circ2 = QuantumCircuit(2, 2)
circ2.append(Pauli("XX"), [0, 1])
circ2.measure([0, 1], [0, 1])
print("Circuit with Pauli inserted directly:\n", circ2)

"""
SUMMARY:
- Demonstrates using Operator objects in circuits.
- Steps:
        1. Create an Operator from Pauli "XX".
        2. Append it to a circuit using QuantumCircuit.append().
        3. Show equivalence of directly appending a Pauli (auto-converts).
"""
