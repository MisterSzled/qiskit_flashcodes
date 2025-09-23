# Demonstrate classical feedforward with if-else control
from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Two qubits, two classical bits
qubits = QuantumRegister(2)
clbits = ClassicalRegister(2)
circuit = QuantumCircuit(qubits, clbits)

(q0, q1) = qubits
(c0, c1) = clbits

print("Step 1: Apply Hadamard to q0 (creates superposition).")
circuit.h(q0)

print("Step 2: Measure q0 into c0.")
circuit.measure(q0, c0)

print("Step 3: Conditional operation on q1.")
with circuit.if_test((c0, 1)) as else_:  # if c0 == 1
    circuit.h(q1)  # apply H
with else_:  # else branch (if c0 != 1)
    circuit.x(q1)  # apply X

print("Step 4: Measure q1 into c1.")
circuit.measure(q1, c1)

print("\nCircuit created:\n", circuit)

"""
SUMMARY:
- Demonstrates if-else branching in circuits.
- Steps:
        1. Put q0 into superposition.
        2. Measure q0 into c0.
        3. If c0 == 1 → apply H to q1.
                Else → apply X to q1.
        4. Measure q1.
"""
