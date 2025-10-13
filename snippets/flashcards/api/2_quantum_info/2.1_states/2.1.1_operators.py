"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Quantum Information Operators (qiskit.quantum_info)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
What does the `Operator` class represent in Qiskit?

a. A symbolic algebraic operator with no numerical matrix.  
b. A dense matrix representation of a linear operator acting on a quantum system.  
c. A sparse Pauli-basis operator optimized for simulation.  
d. A Clifford element restricted to unitary Pauli matrices.  

# Minimal runnable example using `Operator`:
"""
from qiskit.quantum_info import Operator
from qiskit.circuit.library import HGate

op = Operator(HGate())
print("Q1 demo matrix:\n", op.data)

# ---------------------------------------------------------------
"""
# Question 2
Which statement about the `Pauli` class is correct?

a. `Pauli` only stores real-valued matrices.  
b. `Pauli("XZ")` constructs a two-qubit operator X⊗Z.  
c. `Pauli` objects cannot be multiplied.  
d. `Pauli` automatically normalizes its phase to 1.  

# Minimal runnable example creating and multiplying Paulis:
"""
from qiskit.quantum_info import Pauli

p1 = Pauli("XZ")
p2 = Pauli("IX")
print("Q2 demo:", (p1 @ p2).to_label())

# ---------------------------------------------------------------
"""
# Question 3
What does `SparsePauliOp.from_list()` create?

a. A dense `Operator` with full matrix data.  
b. A sparse Pauli-basis operator from (label, coeff) pairs.  
c. A `PauliList` without coefficients.  
d. A Clifford operator expressed in the Pauli basis.  

# Minimal runnable example:
"""
from qiskit.quantum_info import SparsePauliOp

op = SparsePauliOp.from_list([("ZI", 1), ("XZ", 0.5j)])
print("Q3 demo paulis:", op.paulis.to_labels(), "coeffs:", op.coeffs)

# ---------------------------------------------------------------
"""
# Question 4
Which is TRUE about the `PauliList` class?

a. It stores a collection of Pauli strings without coefficients.  
b. It automatically enforces Hermiticity of all elements.  
c. It cannot be indexed.  
d. It performs symbolic algebra.  

# Minimal runnable example:
"""
from qiskit.quantum_info import PauliList

plist = PauliList(["XI", "ZZ"])
print("Q4 demo first Pauli:", plist[0], "count:", len(plist))

# ---------------------------------------------------------------
"""
# Question 5
What does the `Clifford` class represent?

a. A general non-unitary linear operator.  
b. An N-qubit unitary operator from the Clifford group.  
c. A symbolic circuit template.  
d. A subclass of `SparsePauliOp`.  

# Minimal runnable example:
"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Clifford

qc = QuantumCircuit(1)
qc.h(0)
c = Clifford(qc)

print("Q5 demo Clifford is unitary:", c.is_unitary())

# ---------------------------------------------------------------
"""
# Question 6
Which description fits `ScalarOp` best?

a. Represents a scalar multiple of the identity operator.  
b. Represents a scalar multiple of a Pauli operator.  
c. Represents a Clifford conjugation map.  
d. Deprecated in Qiskit 2.x.  

# Minimal runnable example:
"""
from qiskit.quantum_info import ScalarOp

s = ScalarOp(2, 3.0)
print("Q6 demo dim:", s.dim, "coeff:", s.coeff)

# ---------------------------------------------------------------
"""
# Question 7
What is the role of the `CNOTDihedral` class in Qiskit?

a. To generate a random Clifford operator.  
b. To represent N-qubit unitaries composed of CNOT, X, and T gates.  
c. To implement diagonal phase operators only.  
d. To perform symbolic CNOT algebra.  

# Minimal runnable example:
"""
from qiskit.quantum_info import CNOTDihedral

qc = QuantumCircuit(2)
cd = CNOTDihedral(qc)
print("Q7 demo unitary shape:", cd.to_matrix().shape)

# ---------------------------------------------------------------
"""
# Question 8
What does `PauliLindbladMap` represent?

a. A list of Lindblad operators for a density-matrix evolution.  
b. A classical stochastic map over bit strings.  
c. A Pauli-basis representation of a Lindbladian superoperator.  
d. A Clifford noise model.  

# Minimal runnable example:
"""
from qiskit.quantum_info import PauliLindbladMap

plm = PauliLindbladMap.from_list([("X", 0.1), ("Z", 0.2)])
print("Q8 demo decay rates:", plm)

# ---------------------------------------------------------------
"""
# Question 9
Which of the following best describes `QubitSparsePauliList`?

a. A dense matrix representation of Paulis.  
b. A list of phase-less Pauli operators in a qubit-sparse format.  
c. A list of Clifford gates on disjoint qubits.  
d. A deprecated alias of `PauliList`.  

# Minimal runnable example:
"""
from qiskit.quantum_info import QubitSparsePauliList

qlist = QubitSparsePauliList(["XI", "ZZ"])
print("Q9 demo count:", len(qlist), "first:", qlist[0])

# ---------------------------------------------------------------
"""
# Question 10
What does `get_clifford_gate_names()` return?

a. The list of valid Clifford gate names.  
b. A mapping from Clifford gates to circuits.  
c. Only the single-qubit Clifford gate names.  
d. A list of deprecated Clifford gates.  

# Minimal runnable example:
"""
from qiskit.quantum_info import get_clifford_gate_names

names = get_clifford_gate_names()
print("Q10 demo Clifford gate names sample:", names[:5])

# ---------------------------------------------------------------
"""
Answer Key Summary
Q1: b  
Q2: b  
Q3: b  
Q4: a  
Q5: b  
Q6: a  
Q7: b  
Q8: c  
Q9: b  
Q10: a  
"""
