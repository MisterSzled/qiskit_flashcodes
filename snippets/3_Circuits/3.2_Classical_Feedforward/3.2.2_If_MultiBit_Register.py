# Demonstrate conditional operations on multiple classical bits
from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Three qubits, three classical bits
qubits = QuantumRegister(3)
clbits = ClassicalRegister(3)
circuit = QuantumCircuit(qubits, clbits)

(q0, q1, q2) = qubits
(c0, c1, c2) = clbits

print("Step 1: Apply Hadamard to q0 and q1.")
circuit.h([q0, q1])

print("Step 2: Measure q0 into c0 and q1 into c1.")
circuit.measure(q0, c0)
circuit.measure(q1, c1)

print("Step 3: If classical register == 0b001, apply X on q2.")
with circuit.if_test((clbits, 0b001)):  # condition: c2=1, c1=0, c0=0
    circuit.x(q2)

print("Step 4: Measure q2 into c2.")
circuit.measure(q2, c2)

print("\nCircuit created:\n", circuit)

"""
SUMMARY:
- Demonstrates conditioning on multiple classical bits at once.
- Steps:
        1. Apply Hadamards to q0 and q1.
        2. Measure them into c0 and c1.
        3. If register == 0b001, apply X to q2.
        4. Measure q2.
"""
