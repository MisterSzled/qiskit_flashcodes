# Flashcard 2.2.2: Convert Statevector to DensityMatrix
# Demonstrates:
# - Converting a pure statevector into a density matrix
# - Rendering the density matrix in LaTeX

from math import pi
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, DensityMatrix

# Build same state as before
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(pi / 2, 0, 1)
psi = Statevector(qc)

# Step 1: Convert to DensityMatrix
rho = DensityMatrix(psi)
print("[INFO] Converted Statevector to DensityMatrix.")

# Step 2: Draw density matrix as Text - Latex doesn't format nicely on the terminal
latex_matrix = rho.draw("text")
print("[RESULT] Text matrix representation:\n", latex_matrix)

"""
SUMMARY:
- Demonstrates conversion between statevector and density matrix.
- Steps:
        1. Build a 2-qubit circuit and create a Statevector.
        2. Convert the statevector into a density matrix with `DensityMatrix(psi)`.
        3a. Use `.draw("text")` for matrix-style text output.
        3b. Use `.draw("latex")` for matrix-style LaTeX output.
"""
