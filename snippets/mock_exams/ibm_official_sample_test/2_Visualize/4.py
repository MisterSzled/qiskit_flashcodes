"""
Qiskit v2.x Exam Flashcard

Section 2: Visualize quantum circuits, measurements, and states

Question 4:
Which one of the following images is the output from the code below?

        from qiskit import *
        qubits = QuantumRegister(2)
        clbits = ClassicalRegister(2)
        circuit = QuantumCircuit(qubits, clbits)
        (q0, q1) = qubits
        (c0, c1) = clbits
        circuit.h(q0)
        circuit.measure(q0, c0)
        with circuit.if_test((c0, 1)) as else_:
                circuit.h(q1)
        with else_:
                circuit.x(q1)
        circuit.measure(q1, c1)
        circuit.draw(output="mpl")

Choices:
a. [Circuit image A]
b. [Circuit image B]
c. [Circuit image C]
d. [Circuit image D]

"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt

# --- Build the circuit as in the exam snippet ---
qubits = QuantumRegister(2)
clbits = ClassicalRegister(2)
circuit = QuantumCircuit(qubits, clbits)

(q0, q1) = qubits
(c0, c1) = clbits

circuit.h(q0)          # Hadamard on first qubit
circuit.measure(q0, c0)

# Conditional blocks (if/else based on c0)
with circuit.if_test((c0, 1)) as else_:
        circuit.h(q1)
with else_:
        circuit.x(q1)

circuit.measure(q1, c1)

# --- Draw circuit (mpl output) ---
print(circuit)
circuit.draw(output="mpl", filename="circuit.png")

"""
SUMMARY:
        - Builds a 2-qubit, 2-classical-bit circuit.
        - Applies H on q0, then measures into c0.
        - If c0 == 1 → apply H on q1.
        - Else       → apply X on q1.
        - Finally measure q1 into c1.
        - The exam question tests recognition of the circuit diagram produced.

        - c0_0=0x1 means "does classical register 0 (c0) 0th bit(_0) equal 1 (0x1 in hex)
"""
