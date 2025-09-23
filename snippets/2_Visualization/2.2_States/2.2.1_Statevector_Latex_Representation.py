# Flashcard 2.2.1: Render a Statevector in LaTeX format
# Demonstrates:
# - Drawing a quantum state in ket-notation (LaTeX)
# - Switching to "latex_source" mode to get raw LaTeX code

from math import pi
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Build same Bell-like state
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(pi / 2, 0, 1)
psi = Statevector(qc)

# Step 1: LaTeX representation
# In Jupyter this displays pretty math. In scripts, it still produces text.
latex_output = psi.draw("latex")
print("[RESULT] LaTeX ket-notation representation:\n", latex_output)

# Step 2: Raw LaTeX source string
latex_src = psi.draw("latex_source")
print("[RESULT] Raw LaTeX source string:\n", latex_src)

"""
SUMMARY:
- Demonstrates visualizing a statevector in LaTeX formats.
- Steps:
        1. Create a 2-qubit statevector from a circuit.
        2. Use `.draw("latex")` for ket-notation output.
        3. Use `.draw("latex_source")` to obtain raw LaTeX code as a string.
"""
