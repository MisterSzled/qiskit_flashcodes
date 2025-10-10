"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Particular Quantum Circuits (qiskit.circuit.library)
"""

# ---------------------------------------------------------------
"""
# Question 1
Which of the following best describes the purpose of the `fourier_checking()` circuit in Qiskit?

a. It performs phase estimation for a unitary operator.  
b. It checks whether two Boolean functions f and g are correlated in the Fourier basis.  
c. It measures the overlap between two arbitrary unitary matrices.  
d. It implements the Grover search oracle with Fourier encoding.  
"""

from qiskit.circuit.library import fourier_checking

# Encode Boolean values as ±1 for DiagonalGate
f = [1, 1, 1, 1]      # f(x)=0 → +1
g = [-1, -1, -1, -1]  # g(x)=1 → -1

qc = fourier_checking(f, g)
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 2
What does the `iqp()` circuit construct in Qiskit?

a. A circuit that estimates the eigenphases of a Hamiltonian.  
b. A variational ansatz circuit for optimization problems.  
c. An instantaneous quantum polynomial time (IQP) circuit defined by given interactions.  
d. A graph state preparation circuit based on adjacency matrices.  
"""

from qiskit.circuit.library import iqp
import numpy as np

# Generate a random symmetric 3x3 matrix
A = np.random.rand(3, 3)
interactions = np.pi * (A + A.T) / 2  # Symmetrize

qc = iqp(interactions)
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 3
What is the main purpose of the `phase_estimation()` circuit in Qiskit?

a. To estimate the phase (eigenvalue) of a unitary operator.  
b. To perform modular exponentiation.  
c. To prepare a graph state.  
d. To compute a Fourier transform of a random unitary.  
"""

from qiskit.circuit.library import phase_estimation
from qiskit.circuit.library import HGate

qc = phase_estimation(3, HGate())
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 4
Which Qiskit circuit construction is commonly used to benchmark quantum processors using model circuits of specific depth?

a. random_iqp()  
b. quantum_volume()  
c. hidden_linear_function()  
d. grover_operator()  
"""

from qiskit.circuit.library import quantum_volume

qc = quantum_volume(num_qubits=3, depth=3)
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 5
Which gate represents a graph state based on an adjacency matrix?

a. PauliEvolutionGate  
b. GraphStateGate  
c. UnitaryOverlapGate  
d. HamiltonianGate  
"""

from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import GraphStateGate
import numpy as np

adj = np.array([[0,1,0],[1,0,1],[0,1,0]])
qc = QuantumCircuit(3)
qc.append(GraphStateGate(adj), range(3))
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 6
What type of operation does the `PauliEvolutionGate` represent?

a. A non-unitary measurement channel.  
b. The time-evolution of an operator consisting of Pauli terms.  
c. A circuit for Fourier checking between Pauli functions.  
d. A data-encoding feature map for Pauli-Z observables.  
"""

from qiskit.circuit.library import PauliEvolutionGate
from qiskit.quantum_info import SparsePauliOp

op = SparsePauliOp(["XX", "YY"])
qc = QuantumCircuit(2)
qc.append(PauliEvolutionGate(op, time=0.5), range(2))
qc.draw('mpl')

# ---------------------------------------------------------------
"""
# Question 7
Which of the following correctly describes an N-local circuit in Qiskit?

a. A variational circuit composed of local rotation and entanglement layers.  
b. A random unitary circuit used for IQP benchmarking.  
c. A circuit implementing a quantum Fourier transform.  
d. A phase oracle circuit that acts on n logical qubits.  
"""

from qiskit.circuit.library import efficient_su2
qc = efficient_su2(3)
qc.draw('mpl')

# ---------------------------------------------------------------
"""
# Question 8
Which data-encoding circuit encodes classical data as a second-order Pauli-Z evolution?

a. z_feature_map()  
b. pauli_feature_map()  
c. zz_feature_map()  
d. real_amplitudes()  
"""

from qiskit.circuit.library import zz_feature_map
qc = zz_feature_map(feature_dimension=2)
qc.draw('mpl')

# ---------------------------------------------------------------
"""
# Question 9
What is the purpose of the `StatePreparation` circuit in Qiskit?

a. To apply a feature map encoding to a classical dataset.  
b. To prepare a quantum state with specified complex amplitudes.  
c. To perform measurement of all qubits into a classical register.  
d. To simulate the evolution of a given Hamiltonian operator.  
"""

from qiskit.circuit.library import StatePreparation
from qiskit import QuantumCircuit

params = [1/2, 1/2, 1/2, 1/2]
prep = StatePreparation(params)
qc = QuantumCircuit(prep.num_qubits)
qc.append(prep, range(prep.num_qubits))
qc.draw('mpl')

# ---------------------------------------------------------------
"""
# Question 10
Which gate implements a phase-flip oracle that applies (-1)^{f(x)} to computational basis states?

a. BitFlipOracleGate  
b. PhaseOracleGate  
c. QuantumVolumeGate  
d. GroverOperatorGate  
"""

from qiskit.circuit.library import PhaseOracleGate

oracle = PhaseOracleGate('(x & ~y) | z')
qc = QuantumCircuit(3)
qc.append(oracle, range(3))
qc.draw('mpl')

# ---------------------------------------------------------------
"""
Answer Key Summary
------------------
1. b  
2. c  
3. a  
4. b  
5. b  
6. b  
7. a  
8. c  
9. b  
10. b  
"""
