"""
2. Applying the Qiskit ZGate to a qubit in state |1⟩ introduces which global phase?
a. 0 phase
b. π/4 phase
c. π/2 phase
d. π phase
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

# Prepare |1> then apply T
qc = QuantumCircuit(1)
qc.x(0)   # |0> -> |1>
qc.z(0)   # T gate on the qubit

# Get final statevector
state = Statevector.from_instruction(qc)
amp = state.data[1]  # amplitude of |1>

phase_rad = np.angle(amp)

print("State:", state)
print("Phase (radians):", phase_rad)