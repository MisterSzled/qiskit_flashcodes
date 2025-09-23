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

# Step 2: Draw density matrix as LaTeX
latex_matrix = rho.draw("latex")
print("[RESULT] LaTeX matrix representation:\n", latex_matrix)

"""
SUMMARY:
- Demonstrates conversion between statevector and density matrix.
- Steps:
        1. Build a 2-qubit circuit and create a Statevector.
        2. Convert the statevector into a density matrix with `DensityMatrix(psi)`.
        3. Use `.draw("latex")` for matrix-style LaTeX output.
"""
