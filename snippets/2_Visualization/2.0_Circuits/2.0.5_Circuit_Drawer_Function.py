# 2.0.5 Circuit Drawer Function
# Demonstrates standalone circuit_drawer function.

from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)

# Use circuit_drawer instead of circuit.draw
circuit_drawer(circuit, output="mpl", filename="drawer_func.png", plot_barriers=False)
print("Circuit diagram drawn with circuit_drawer() saved as drawer_func.png")

"""
SUMMARY:
- Demonstrates qiskit.visualization.circuit_drawer().
- Steps:
        1. Build 2-qubit circuit with H and CX.
        2. Call circuit_drawer(circuit, output="mpl").
        3. Save diagram as drawer_func.png.
        4. Equivalent to circuit.draw() but function-based.
"""
