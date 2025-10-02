"""
Qiskit v2.x Exam Flashcard

Question 2:
Applying the Qiskit TGate to a qubit in state |1> introduces which global phase?

a. π/2 phase
b. -π/2 phase
c. -π/4 phase
d. π/4 phase

"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

# Prepare |1> then apply T
qc = QuantumCircuit(1)
qc.x(0)   # |0> -> |1>
qc.t(0)   # T gate on the qubit

# Get final statevector
state = Statevector.from_instruction(qc)
amp = state.data[1]  # amplitude of |1>

phase_rad = np.angle(amp)

print("State:", state)
print("Phase (radians):", phase_rad)

"""
SUMMARY (what this shows):
        - After applying T to |1>, the amplitude becomes a complex number with real=imag≈0.70710678.
        - 0.70710678 ≈ sqrt(2)/2 (not π/4). The complex number equals cos(π/4)+i sin(π/4).
        - The polar (phase) of the amplitude is π/4 radians (≈ 45°), and its magnitude is 1, so the amplitude = e^{iπ/4}.
        - Thus the T gate multiplies |1> by the complex factor e^{iπ/4}.
"""
