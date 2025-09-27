# 2.0.3 Draw BitOrder And Barriers
# Demonstrates reverse_bits and plot_barriers options.

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Create multiple registers
q_a = QuantumRegister(3, name="a")
q_b = QuantumRegister(2, name="b")
c_a = ClassicalRegister(3)
c_b = ClassicalRegister(2)
circuit = QuantumCircuit(q_a, q_b, c_a, c_b)

# Apply some gates + barriers
circuit.x(q_a[1])
circuit.barrier()
circuit.h(q_a)
circuit.barrier(q_b)
circuit.measure(q_a, c_a)
circuit.measure(q_b, c_b)

print("Default circuit (with barriers):")
print(circuit.draw(output="text"))

print("\nReversed bit order:")
print(circuit.draw(output="text", reverse_bits=True))

print("\nWithout barriers:")
print(circuit.draw(output="text", plot_barriers=False))
circuit.draw(output="mpl", filename="circuit.png")
"""
SUMMARY:
- Demonstrates bit order reversal and barrier control in circuit diagrams.
- Steps:
        1. Build circuit with 2 quantum + 2 classical registers.
        2. Insert barriers between operations.
        3. Draw normally → includes barriers.
        4. Draw with reverse_bits=True → order flipped.
        5. Draw with plot_barriers=False → barriers omitted.
"""
