# Flashcard 2.2.3: Plot state on Bloch sphere and Qsphere
# Demonstrates:
# - Visualizing a quantum state using Bloch sphere and Qsphere
# - Saving or showing matplotlib figures explicitly

from math import pi
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_bloch_multivector, plot_state_qsphere

# Step 1: Build a statevector
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(pi / 2, 0, 1)
psi = Statevector(qc)
print("[INFO] Statevector prepared.")

# Step 2: Plot on Bloch sphere (for each qubit)
fig_bloch = plot_state_bloch_multivector(psi, title="Bloch Sphere of Psi")
print("[INFO] Bloch sphere plot created.")
fig_bloch.show()     # Opens interactive window if supported
# fig_bloch.savefig("bloch.png")

# Step 3: Plot on Qsphere
fig_qsphere = plot_state_qsphere(psi, title="Qsphere of Psi")
print("[INFO] Qsphere plot created.")
fig_qsphere.show()   # Opens interactive window
# fig_qsphere.savefig("qsphere.png")

"""
SUMMARY:
- Demonstrates visualizing quantum states using Bloch sphere and Qsphere.
- Steps:
        1. Build a 2-qubit circuit and generate a statevector.
        2. Use `plot_state_bloch_multivector` for Bloch sphere visualization.
        3. Use `plot_state_qsphere` for Qsphere visualization.
        4. Show or save plots explicitly in scripts.
"""
