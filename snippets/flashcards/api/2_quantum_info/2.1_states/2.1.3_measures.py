"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Quantum Information Measures (qiskit.quantum_info)
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
What does `average_gate_fidelity(channel, target)` compute?

a. The probability that a gate acts identically on every state.  
b. The average state fidelity between an ideal and noisy channel over all pure states.  
c. The diamond norm of two operators.  
d. The trace distance between two quantum channels.  

# Minimal runnable example:
"""
from qiskit.quantum_info import average_gate_fidelity, SuperOp
from qiskit.circuit.library import XGate

noisy = SuperOp(XGate())
fid = average_gate_fidelity(noisy, XGate())
print("Q1 demo average gate fidelity:", fid)

# ---------------------------------------------------------------
"""
# Question 2
Which function computes the process fidelity between two channels?

a. average_gate_fidelity()  
b. process_fidelity()  
c. gate_error()  
d. diamond_norm()  

# Minimal runnable example:
"""
from qiskit.quantum_info import process_fidelity

fid = process_fidelity(SuperOp(XGate()), XGate())
print("Q2 demo process fidelity:", fid)

# ---------------------------------------------------------------
"""
# Question 3
The process fidelity between channels E and U is equal to the fidelity between:

a. Their Choi matrices normalized by the channel dimension.  
b. Their unitary matrices directly.  
c. Their Kraus representations.  
d. Their eigenvalues.  

# Minimal runnable example:
"""
from qiskit.quantum_info import Choi
fid = process_fidelity(Choi(XGate()), XGate())
print("Q3 demo process fidelity (via Choi):", fid)

# ---------------------------------------------------------------
"""
# Question 4
What does `gate_error(channel, target)` return?

a. The difference between ideal and noisy process fidelities.  
b. The average gate infidelity, i.e., 1 - F_avg(E, U).  
c. The diamond norm of the error.  
d. The entropy of the channel.  

# Minimal runnable example:
"""
from qiskit.quantum_info import gate_error

err = gate_error(SuperOp(XGate()), XGate())
print("Q4 demo gate error:", err)

# ---------------------------------------------------------------
"""
# Question 6
What does `state_fidelity(state1, state2)` measure?

a. The Hilbert-Schmidt inner product of the density matrices.  
b. The closeness of two quantum states (1 for identical, 0 for orthogonal).  
c. The entropy difference between two states.  
d. The gate infidelity.  

# Minimal runnable example:
"""
from qiskit.quantum_info import Statevector, state_fidelity

psi = Statevector.from_label("00")
phi = Statevector.from_label("00")
print("Q6 demo state fidelity:", state_fidelity(psi, phi))

# ---------------------------------------------------------------
"""
# Question 7
What quantity does `purity(state)` calculate?

a. Tr[p²], measuring how mixed a quantum state is.  
b. The determinant of the density matrix.  
c. The entropy of a state.  
d. The norm of the statevector.  

# Minimal runnable example:
"""
from qiskit.quantum_info import DensityMatrix, purity

rho = DensityMatrix.from_label("00")
print("Q7 demo purity:", purity(rho))

# ---------------------------------------------------------------
"""
# Question 8
What is the purpose of the `concurrence(state)` function?

a. It measures the entanglement of a 2-qubit quantum state.  
b. It measures the fidelity of two channels.  
c. It returns the purity of a bipartite state.  
d. It computes the logarithmic negativity.  

# Minimal runnable example:
"""
from qiskit.quantum_info import concurrence
from qiskit.circuit.library import CXGate

bell = Statevector.from_instruction(CXGate())
print("Q8 demo concurrence:", concurrence(bell))

# ---------------------------------------------------------------
"""
# Question 9
Which expression defines the von Neumann entropy computed by `entropy(state)`?

a. S(p) = -Tr[p log(p)]  
b. S(p) = Tr[p²]  
c. S(p) = log(det(p))  
d. S(p) = Tr[p log₂(p)]²  

# Minimal runnable example:
"""
from qiskit.quantum_info import entropy

rho = DensityMatrix(Statevector.from_label("00"))
print("Q9 demo entropy:", entropy(rho))

# ---------------------------------------------------------------
"""
# Question 10
What does `mutual_information(state)` return for a bipartite system?

a. I(p_AB) = S(p_A) + S(p_B) - S(p_AB).  
b. I(p_AB) = Tr[p_A p_B].  
c. I(p_AB) = log(det(p_AB)).  
d. I(p_AB) = Tr[p_AB²].  

# Minimal runnable example:
"""
from qiskit.quantum_info import mutual_information, partial_trace

# Create simple product state
rho_AB = DensityMatrix.from_label("00")
print("Q10 demo mutual information:", mutual_information(rho_AB))

# ---------------------------------------------------------------
"""
Answer Key Summary
Q1: b  
Q2: b  
Q3: a  
Q4: b
Q6: b  
Q7: a  
Q8: a  
Q9: a  
Q10: a  
"""
