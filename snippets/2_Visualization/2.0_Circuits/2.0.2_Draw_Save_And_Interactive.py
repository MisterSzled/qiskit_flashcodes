# 2.0.2 Draw Save And Interactive
# Demonstrates saving diagrams to file and interactive display.

from qiskit import QuantumCircuit

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)

# Save as PNG using matplotlib renderer
circuit.draw(output="mpl", filename="circuit.png")
print("Circuit diagram saved as circuit.png (matplotlib).")

# Save as LaTeX image
# circuit.draw(output="latex", filename="circuit_latex.png")
print("Circuit diagram saved as circuit_latex.png (LaTeX).")

# Interactive window (may not work in all environments)
# circuit.draw(output="mpl", interactive=True)

"""
SUMMARY:
- Shows saving and interactive options for draw().
- Steps:
        1. Build 2-qubit H+CX circuit.
        2. Save diagram as PNG with mpl renderer.
        3. Save diagram as PNG with latex renderer.
        4. Optionally display in interactive window (commented out).
"""
