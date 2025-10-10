# Demonstrating conversion of various Qiskit classes into Operator objects.

import numpy as np
from qiskit.circuit.library import CXGate, RXGate
from qiskit.quantum_info import Operator, Pauli
from qiskit.circuit import QuantumCircuit

# Convert from a Pauli object
pauli_xx = Pauli("XX")   # Pauli operator "X ⊗ X"
op_from_pauli = Operator(pauli_xx)
print("Operator from Pauli XX:\n", op_from_pauli.data, "\n")

# Convert from a Gate object (CNOT)
op_from_cx = Operator(CXGate())  # CXGate is a 2-qubit controlled-X gate
print("Operator from CXGate:\n", op_from_cx.data, "\n")

# Convert from a parameterized Gate (RX rotation)
op_from_rx = Operator(RXGate(np.pi / 2))  # RX(π/2)
print("Operator from RXGate(π/2):\n", op_from_rx.data, "\n")

# Convert from a QuantumCircuit
circ = QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
op_from_circ = Operator(circ)  # Implicit unitary simulation
print("Operator from 3-qubit circuit:\n", op_from_circ.data, "\n")

"""
SUMMARY:
- Shows how to convert Pauli, Gate, RXGate, and full QuantumCircuit into Operator.
- Steps:
        1. Define each object (Pauli, CXGate, RXGate, QuantumCircuit).
        2. Pass it to Operator() constructor.
        3. Print the resulting dense matrix.
"""
