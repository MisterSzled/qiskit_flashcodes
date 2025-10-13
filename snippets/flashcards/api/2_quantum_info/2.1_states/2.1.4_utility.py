# ===============================================================
# Qiskit 2.x Mock Exam — Quantum Information: Utility Functions
# ===============================================================

# ---------------------------------------------------------------
"""
Question 1
Given a 2-qubit state |ψ⟩ = (|00⟩ + |11⟩)/√2 represented as a Statevector,
which Qiskit function correctly returns the reduced density matrix
of the first qubit (i.e., tracing out qubit 1)?

a. partial_trace(psi, [0])
b. partial_trace(psi, [1])
c. partial_trace(psi, [0,1])
d. partial_trace(psi)

Correct answer: b
"""

from qiskit.quantum_info import Statevector, partial_trace
from numpy import sqrt

psi = Statevector([1/sqrt(2), 0, 0, 1/sqrt(2)])
dm0 = partial_trace(psi, [1])
print(dm0)
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 2
Which function provides the Schmidt coefficients and vectors
for a pure bipartite statevector in Qiskit?

a. partial_trace(state, qargs)
b. schmidt_decomposition(state, qargs)
c. mutual_information(state)
d. entropy(state)

Correct answer: b
"""

from qiskit.quantum_info import schmidt_decomposition
# (Example use)
# schmidt_decomposition(Statevector(...), [1])
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 3
Compute the Shannon entropy of a probability vector p = [0.5, 0.5].
What is the expected result in bits?

a. 0
b. 0.5
c. 1.0
d. 2.0

Correct answer: c
"""

from qiskit.quantum_info import shannon_entropy
print(shannon_entropy([0.5, 0.5]))  # Expect 1.0
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 4
What does qiskit.quantum_info.commutator(a, b) compute?

a. [a, b] = a @ b - b @ a
b. {a, b} = a @ b + b @ a
c. a * b (elementwise)
d. a.conjugate().T @ b

Correct answer: a
"""

from qiskit.quantum_info import Operator, commutator
from qiskit.circuit.library import XGate, ZGate

print(commutator(Operator(XGate()), Operator(ZGate())))
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 5
What is returned by qiskit.quantum_info.anti_commutator(A, B)?

a. [A, B] = AB - BA
b. {A, B} = AB + BA
c. A ⊗ B
d. (A * B).trace()

Correct answer: b
"""

from qiskit.quantum_info import anti_commutator
print(anti_commutator(Operator(XGate()), Operator(ZGate())))
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 6
When commutator=True, the double_commutator(A, B, C) in Qiskit computes:

a. ([[A, B], C] + [A, [B, C]]) / 2
b. ([A, B] + [B, C] + [C, A]) / 3
c. {[A, B], C}
d. [A, [B, [C, A]]]

Correct answer: a
"""

from qiskit.quantum_info import double_commutator
print(double_commutator(Operator(XGate()), Operator(ZGate()), Operator(XGate())))
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 7
Which of the following correctly creates a Qiskit Quaternion object?

a. Quaternion = qiskit.quantum_info.Quaternion
b. Quaternion([1, 0, 0, 0])
c. qiskit.Quaternion()
d. Quaternion(1+0j)

Correct answer: b
"""

from qiskit.quantum_info import Quaternion
q = Quaternion([1, 0, 0, 0])
print(q)
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 8
If all subsystems are traced out in partial_trace(state, qargs),
what does the function return?

a. The zero matrix
b. The trace of the input state (a scalar, usually 1.0)
c. The full density matrix
d. A list of density matrices

Correct answer: b
"""

# Example: trace over all subsystems
print(partial_trace(psi, [0, 1]))
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 9
What does shannon_entropy(pvec, base=2) return if pvec = [1.0, 0.0]?

a. 1
b. 0
c. 2
d. NaN

Correct answer: b
"""

print(shannon_entropy([1.0, 0.0]))  # Expect 0 bits of uncertainty
# ---------------------------------------------------------------


# ---------------------------------------------------------------
"""
Question 10
Which statement about schmidt_decomposition() is TRUE?

a. It only accepts DensityMatrix inputs.
b. It returns a tuple (U, S, V) like np.linalg.svd().
c. It returns a list of (λ, |u⟩, |v⟩) triples, where λ are Schmidt coefficients.
d. It traces out the specified subsystems automatically.

Correct answer: c
"""

# schmidt_decomposition returns [(λ1, |u1⟩, |v1⟩), ...]
# Example:
# from qiskit.quantum_info import Statevector
# schmidt_decomposition(Statevector([1/sqrt(2), 0, 0, 1/sqrt(2)]), [1])
# ---------------------------------------------------------------
