# 2.0.0 Draw Circuit Basics
# Demonstrates difference between print(circuit) and circuit.draw().

from qiskit import QuantumCircuit

# Build a simple circuit: 3 qubits, 3 classical bits
circuit = QuantumCircuit(3, 3)
circuit.x(1)                  # Apply X gate to qubit 1
circuit.h(range(3))           # Apply H gate to all qubits
circuit.cx(0, 1)              # Apply CNOT with control 0, target 1
circuit.measure(range(3), range(3))  # Measure all qubits into all bits

print("Circuit printed directly (ASCII art):")
print(circuit)   # Prints diagram to stdout (returns None)

print("\nCircuit using circuit.draw():")
print(circuit.draw())   # Returns a TextDrawing object (ASCII art)

"""
SUMMARY:
- Demonstrates printing vs drawing circuits.
- Steps:
        1. Build 3-qubit circuit with X, H, CX, and measurement.
        2. Print(circuit) → side effect: ASCII diagram, returns None.
        3. circuit.draw() → returns TextDrawing object, prints diagram explicitly.
"""
