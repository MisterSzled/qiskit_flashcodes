# Flashcard 2.2.4: Plot state using Cityscape and Pauli vector
# Demonstrates:
# - State visualization with bar charts
# - Customizing title, figsize, and colors
# - Saving plots to PNG files for use in headless environments

from math import pi
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_city, plot_state_paulivec

# Step 1: Build statevector
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(pi / 2, 0, 1)
psi = Statevector(qc)
print("[INFO] Statevector prepared.")

# Step 2: Cityscape plot
fig_city = plot_state_city(psi, title="Cityscape of Psi", figsize=(8, 6), color=["blue", "orange"])
print("[INFO] Cityscape plot created.")
fig_city.savefig("cityscape.png")  # Save instead of show
print("[INFO] Cityscape plot saved as cityscape.png")

# Step 3: Pauli vector plot
fig_pauli = plot_state_paulivec(psi, title="Pauli vector of Psi", figsize=(8, 6), color=["green", "red"])
print("[INFO] Pauli vector plot created.")
fig_pauli.savefig("paulivec.png")  # Save instead of show
print("[INFO] Pauli vector plot saved as paulivec.png")

"""
SUMMARY:
- Demonstrates additional state visualization options.
- Steps:
        1. Build a 2-qubit circuit and generate a statevector.
        2. Use `plot_state_city` for a cityscape (matrix element magnitude + phase).
        3. Use `plot_state_paulivec` for Pauli vector representation.
        4. Customize output with `title`, `figsize`, and `color` arguments.
        5. Save plots to PNG files instead of requiring a GUI.
"""
