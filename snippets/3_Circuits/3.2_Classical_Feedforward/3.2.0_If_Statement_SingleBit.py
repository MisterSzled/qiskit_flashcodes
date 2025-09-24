# Demonstrate classical feedforward with a single-bit condition
from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Create one qubit and one classical bit
qubits = QuantumRegister(1)
clbits = ClassicalRegister(1)
circuit = QuantumCircuit(qubits, clbits)

(q0,) = qubits  # unpack qubit
(c0,) = clbits  # unpack classical bit

print("Step 1: Apply Hadamard gate to create superposition.")
circuit.h(q0)  # places qubit in |0> + |1> state

print("Step 2: Measure the qubit into classical bit c0.")
circuit.measure(q0, c0)  # collapse to 0 or 1

print("Step 3: If measurement == 1, apply X to flip back to |0>.")
with circuit.if_test((c0, 1)):  # condition: if c0 == 1
        circuit.x(q0)

print("Step 4: Measure again to confirm qubit is reset to |0>.")
circuit.measure(q0, c0)

print("\nCircuit created:\n", circuit)

"""
SUMMARY:
- Demonstrates classical feedforward with an if-statement on a single measurement bit.
- Steps:
        1. Apply Hadamard gate to qubit.
        2. Measure result into classical bit.
        3. If result == 1, apply X gate to flip back to |0>.
        4. Measure again, ensuring final result is always 0.
"""
