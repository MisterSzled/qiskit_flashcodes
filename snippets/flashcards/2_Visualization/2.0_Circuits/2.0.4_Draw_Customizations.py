# 2.0.4 Draw Customizations
# Demonstrates renderer-specific customization options.

from qiskit import QuantumCircuit

# Build a 1-qubit circuit with many H gates
circuit = QuantumCircuit(1)
for _ in range(10):
    circuit.h(0)

# Fold text output to 40 chars per line
print("Folded text diagram (40 chars per line):")
print(circuit.draw(output="text", fold=40))

# Custom style for matplotlib: change background color
style = {"backgroundcolor": "lightgreen"}
circuit.draw(output="mpl", style=style, filename="styled_circuit.png")
print("\nStyled diagram saved as styled_circuit.png with green background.")

# Scale output to half-size (mpl)
circuit.draw(output="mpl", scale=0.5, filename="scaled_circuit.png")
print("Scaled diagram saved as scaled_circuit.png at 0.5x size.")

"""
SUMMARY:
- Shows customizing circuit diagrams.
- Steps:
        1. Build 1-qubit circuit with 10 H gates.
        2. Use fold=40 to wrap long ASCII diagrams.
        3. Use style dict to change mpl rendering (green background).
        4. Use scale=0.5 to shrink mpl diagram output.
"""
