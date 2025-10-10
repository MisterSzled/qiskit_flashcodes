# 2.0.1 Draw Alternative Renderers
# Demonstrates text, matplotlib, and LaTeX renderers.

from qiskit import QuantumCircuit

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)

# Default text renderer
print("Text renderer (default):")
print(circuit.draw(output="text"))

# Matplotlib renderer
print("\nMatplotlib renderer object type:")
print(type(circuit.draw(output="mpl")))  # returns matplotlib.figure.Figure

# LaTeX renderer
print("\nLaTeX renderer object type:")
print(type(circuit.draw(output="latex")))  # returns PIL.Image.Image

"""
SUMMARY:
- Shows different rendering backends for circuit diagrams.
- Steps:
        1. Build 2-qubit circuit (H + CX).
        2. Use draw(output="text") → ASCII art.
        3. Use draw(output="mpl") → matplotlib.Figure object.
        4. Use draw(output="latex") → PIL.Image object.
"""
