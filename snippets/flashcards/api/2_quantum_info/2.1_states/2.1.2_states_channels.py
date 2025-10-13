"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Quantum States and Channels (qiskit.quantum_info)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
What does the `Statevector` class represent in Qiskit?

a. The density matrix representation of a mixed state.  
b. A pure quantum state represented as a complex vector in Hilbert space.  
c. A symbolic description of a circuit.  
d. A stabilizer tableau encoding a Clifford state.  

# Minimal runnable example:
"""
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import HGate

psi = Statevector(HGate())
print("Q1 demo statevector data:", psi.data)

# ---------------------------------------------------------------
"""
# Question 2
Which operation does the method `.probabilities_dict()` perform for a Statevector?

a. Returns a mapping of computational basis states to their measurement probabilities.  
b. Returns the amplitudes directly.  
c. Returns eigenvalues of the density matrix.  
d. Simulates measurement collapse.  

# Minimal runnable example:
"""
psi = Statevector.from_label("00").evolve(HGate(), [0])
print("Q2 demo probabilities:", psi.probabilities_dict())

# ---------------------------------------------------------------
"""
# Question 3
What does the `DensityMatrix` class represent?

a. A statistical mixture or pure state as a positive semi-definite matrix.  
b. A Clifford tableau.  
c. Only diagonal classical probability states.  
d. The tensor product of multiple Statevectors.  

# Minimal runnable example:
"""
from qiskit.quantum_info import DensityMatrix

rho = DensityMatrix.from_label("00")
print("Q3 demo density matrix shape:", rho.data.shape)

# ---------------------------------------------------------------
"""
# Question 4
What distinguishes `StabilizerState` from `Statevector` and `DensityMatrix`?

a. It only represents mixed states.  
b. It represents Clifford-stabilizer states efficiently without amplitudes.  
c. It stores data as a density matrix.  
d. It is used only for parameterized circuits.  

# Minimal runnable example:
"""
from qiskit.quantum_info import StabilizerState
from qiskit.circuit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
stab = StabilizerState(qc)
print("Q4 demo stabilizer tableau shape:", stab)

# ---------------------------------------------------------------
"""
# Question 5
What does the `Choi` class represent in Qiskit?

a. A density matrix on doubled Hilbert space describing a quantum channel.  
b. The Stinespring dilation of a channel.  
c. The Kraus operator list for a channel.  
d. A symbolic channel label.  

# Minimal runnable example:
"""
from qiskit.quantum_info import Choi
from qiskit.circuit.library import XGate

choi = Choi(XGate())
print("Q5 demo Choi shape:", choi.data.shape)

# ---------------------------------------------------------------
"""
# Question 6
What is the `SuperOp` representation of a quantum channel?

a. A unitary operator acting on qubits directly.  
b. The channel represented as a linear map acting on vectorized density matrices.  
c. A list of Kraus operators.  
d. A measurement outcome probability map.  

# Minimal runnable example:
"""
from qiskit.quantum_info import SuperOp

superop = SuperOp(XGate())
print("Q6 demo SuperOp shape:", superop.data.shape)

# ---------------------------------------------------------------
"""
# Question 7
What does the `Kraus` representation consist of?

a. A single matrix that diagonalizes a channel.  
b. One or more matrices {K_i} such that ρ → Σ_i K_i ρ K_i†.  
c. The PTM matrix in the Pauli basis.  
d. A symbolic operator form of the Choi matrix.  

# Minimal runnable example:
"""
from qiskit.quantum_info import Kraus

kraus = Kraus(XGate())
print("Q7 demo number of Kraus ops:", len(kraus.data))

# ---------------------------------------------------------------
"""
# Question 8
Which of the following describes the `Stinespring` representation?

a. It represents a channel as a unitary on system + environment.  
b. It is equivalent to a PTM matrix.  
c. It is a Kraus list in diagonalized form.  
d. It is a symbolic Pauli transfer operator.  

# Minimal runnable example:
"""
from qiskit.quantum_info import Stinespring

st = Stinespring(XGate())
print("Q8 demo Stinespring shape:", st.data.shape)

# ---------------------------------------------------------------
"""
# Question 9
What does the `Chi` representation express?

a. The channel in the Pauli basis using a χ-matrix.  
b. The eigenbasis decomposition of a unitary.  
c. A symbolic Clifford map.  
d. A stochastic classical process.  

# Minimal runnable example:
"""
from qiskit.quantum_info import Chi

chi = Chi(XGate())
print("Q9 demo Chi matrix shape:", chi.data.shape)

# ---------------------------------------------------------------
"""
# Question 10
What is the `PTM` (Pauli Transfer Matrix) representation?

a. A real matrix representing a channel’s action on Pauli operators.  
b. A complex-valued Choi matrix.  
c. The Stinespring dilation.  
d. The eigenbasis of the density operator.  

# Minimal runnable example:
"""
from qiskit.quantum_info import PTM

ptm = PTM(XGate())
print("Q10 demo PTM matrix shape:", ptm.data.shape)

# ---------------------------------------------------------------
"""
Answer Key Summary
Q1: b  
Q2: a  
Q3: a  
Q4: b  
Q5: a  
Q6: b  
Q7: b  
Q8: a  
Q9: a  
Q10: a  
"""
