"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Random Generators (qiskit.quantum_info.random)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
What distribution does `qiskit.quantum_info.random_statevector` use when sampling random statevectors?

a. Uniform distribution over computational basis states.  
b. Gaussian distribution over amplitudes.  
c. Haar-uniform distribution over the unitary group.  
d. Uniform distribution over real-valued amplitudes only.

# Minimal runnable example:
# sv = random_statevector(2, seed=42)
# print(sv.is_unitary())  # should print False, since it's a state, not a unitary
"""
from qiskit.quantum_info import random_statevector

sv = random_statevector(2, seed=42)
print("Norm of statevector:", sv.norm())

# ---------------------------------------------------------------
"""
# Question 2
When using `random_density_matrix`, what does the parameter `method='Bures'` specify?

a. The matrix is generated with real entries only.  
b. Sampling uses the Bures metric instead of the Hilbert-Schmidt metric.  
c. The resulting density matrix is always pure.  
d. It ensures the matrix is diagonal in the Pauli basis.

# Minimal runnable example:
# dm = random_density_matrix(2, method='Bures', seed=1)
# print("Trace:", dm.trace())
"""
from qiskit.quantum_info import random_density_matrix

dm = random_density_matrix(2, method="Bures", seed=1)
print("Trace of density matrix:", dm.trace())

# ---------------------------------------------------------------
"""
# Question 3
What is the purpose of the `rank` argument in `random_density_matrix(dims, rank)`?

a. To control the number of qubits.  
b. To specify the rank (number of nonzero eigenvalues) of the matrix.  
c. To limit the number of samples drawn from the distribution.  
d. To fix the purity to 1/rank.

# Minimal runnable example:
# dm_rank2 = random_density_matrix(4, rank=2, seed=2)
# print("Eigenvalues:", dm_rank2.eigenvalues())
"""
dm_rank2 = random_density_matrix(4, rank=2, seed=2)
print("Rank of generated matrix:", dm_rank2.matrix_rank())

# ---------------------------------------------------------------
"""
# Question 4
`random_unitary(dims)` returns what kind of Qiskit object?

a. Statevector  
b. Operator  
c. UnitaryGate  
d. QuantumCircuit

# Minimal runnable example:
# U = random_unitary(2)
# print(type(U))
"""
from qiskit.quantum_info import random_unitary

U = random_unitary(2, seed=123)
print("Object type:", type(U).__name__)

# ---------------------------------------------------------------
"""
# Question 5
What does `random_hermitian(dims, traceless=True)` guarantee about the output operator?

a. It has unit determinant.  
b. It has zero trace.  
c. It is non-Hermitian.  
d. It commutes with all Pauli operators.

# Minimal runnable example:
# H = random_hermitian(2, traceless=True)
# print("Trace:", H.trace())
"""
from qiskit.quantum_info import random_hermitian

H = random_hermitian(2, traceless=True, seed=5)
print("Trace of Hermitian operator:", H.trace())

# ---------------------------------------------------------------
"""
# Question 6
In `random_pauli(num_qubits, group_phase=True)`, what effect does `group_phase=True` have?

a. Adds a global random phase to each Pauli operator.  
b. Forces all Paulis to be identity.  
c. Produces only real-valued coefficients.  
d. Increases the number of qubits by 1.

# Minimal runnable example:
# p = random_pauli(3, group_phase=True, seed=3)
# print(p)
"""
from qiskit.quantum_info import random_pauli

p = random_pauli(3, group_phase=True, seed=3)
print("Generated Pauli:", p)

# ---------------------------------------------------------------
"""
# Question 7
Which of the following is returned by `random_clifford(num_qubits)`?

a. CliffordGate  
b. Clifford object representing a random stabilizer operation.  
c. Random permutation matrix.  
d. Unitary sampled from the Gaussian unitary ensemble.

# Minimal runnable example:
# C = random_clifford(2, seed=7)
# print("Num qubits:", C.num_qubits)
"""
from qiskit.quantum_info import random_clifford

C = random_clifford(2, seed=7)
print("Random Clifford on", C.num_qubits, "qubits")

# ---------------------------------------------------------------
"""
# Question 8
What kind of object does `random_quantum_channel(input_dims, output_dims)` return?

a. SuperOp  
b. Stinespring  
c. Choi  
d. DensityMatrix

# Minimal runnable example:
# ch = random_quantum_channel(2, 2, seed=0)
# print(type(ch))
"""
from qiskit.quantum_info import random_quantum_channel

ch = random_quantum_channel(2, 2, seed=0)
print("Type:", type(ch).__name__)

# ---------------------------------------------------------------
"""
# Question 9
The `random_cnotdihedral(num_qubits)` function samples from which group?

a. Clifford group  
b. CNOT-Dihedral group  
c. Unitary group U(2^n)  
d. Pauli group

# Minimal runnable example:
# cd = random_cnotdihedral(3, seed=5)
# print(cd)
"""
from qiskit.quantum_info import random_cnotdihedral

cd = random_cnotdihedral(3, seed=5)
print("Random CNOTDihedral element:", cd)

# ---------------------------------------------------------------
"""
# Question 10
What is the purpose of the `phase` argument in `random_pauli_list(num_qubits, size, phase)`?

a. Determines whether to include random ±i phases for each Pauli term.  
b. Controls the number of Paulis generated.  
c. Sets the total phase of the combined operator to zero.  
d. Restricts the output to Hermitian Paulis only.

# Minimal runnable example:
# pl = random_pauli_list(2, size=3, phase=True, seed=9)
# print(pl)
"""
from qiskit.quantum_info import random_pauli_list

pl = random_pauli_list(2, size=3, phase=True, seed=9)
print("Random PauliList:", pl)
