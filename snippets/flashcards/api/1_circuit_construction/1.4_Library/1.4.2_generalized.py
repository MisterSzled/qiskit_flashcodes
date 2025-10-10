"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Generalized Gates (qiskit.circuit.library.generalized_gates)
"""

# ---------------------------------------------------------------
"""
# Question 1
Which statement correctly describes **generalized gates** in Qiskit 2.x?

a. They are fixed-size one- and two-qubit gates that subclass Operation.  
b. They extend standard gates to include variadic and higher-order constructs.  
c. They are only used for measurement operations.  
d. They are hardware-native gates tied to a specific backend.  
"""

from qiskit.circuit.library import DiagonalGate

diagonal = DiagonalGate([1, 1j])
print("Number of qubits:", diagonal.num_qubits)

diagonal2 = DiagonalGate([1, 1, 1, -1])
print("Number of qubits:", diagonal2.num_qubits)

# ---------------------------------------------------------------
"""
# Question 2
Which statement about the DiagonalGate class is correct?

a. It implements a general diagonal operator whose size determines its qubit count.  
b. It always acts on two qubits regardless of input length.  
c. It is non-unitary and cannot be simulated on a Statevector.  
d. It is a subclass of QuantumCircuit used for diagonalization.  
"""

from qiskit.circuit.library import DiagonalGate
from qiskit.quantum_info import Operator

gate = DiagonalGate([1, -1])
matrix = Operator(gate).data

print("Matrix:\n", matrix)

# ---------------------------------------------------------------
"""
# Question 3
What does the PermutationGate class do?

a. Randomly shuffles classical bits in a register.  
b. Applies a reversible mapping that permutes qubits.  
c. Implements stochastic reordering of measurement results.  
d. Reorders operations in a compiled circuit.  
"""

from qiskit.circuit.library import PermutationGate

perm_gate = PermutationGate([1, 0])
print("Permutation matrix:\n", perm_gate.to_matrix())

# ---------------------------------------------------------------
"""
# Question 4
What is the purpose of the MCMTGate in Qiskit 2.x?

a. To build a single-qubit rotation gate controlled by multiple qubits.  
b. To construct a multi-controlled, multi-target operation from a base gate.  
c. To decompose controlled operations into Gray-code CX chains.  
d. To create random controlled operations.  
"""

from qiskit.circuit.library import MCMTGate, XGate

mcmt = MCMTGate(XGate(), num_ctrl_qubits=2, num_target_qubits=1)
print(mcmt)

# ---------------------------------------------------------------
"""
# Question 5
Which gate implements a **multi-controlled phase rotation**?

a. MCPhaseGate  
b. PhaseGate  
c. MSGate  
d. MCXGate  
"""

from qiskit.circuit.library import MCPhaseGate
from math import pi

mcphase = MCPhaseGate(pi / 2, num_ctrl_qubits=2)
print(mcphase)

# ---------------------------------------------------------------
"""
# Question 6
Which of the following gates performs a **Mølmer–Sørensen interaction** between multiple qubits?

a. MSGate  
b. MCXGate  
c. UCGate  
d. DiagonalGate  
"""

from qiskit.circuit.library import MSGate
from qiskit.quantum_info import Operator

ms_gate = MSGate(2, 0.5)
matrix = Operator(ms_gate).data

print("Matrix:\n", matrix)

# ---------------------------------------------------------------
"""
# Question 7
What is the primary difference between the classes `PauliGate` and `LinearFunction`?

a. PauliGate supports only Z operations, while LinearFunction supports any Clifford operation.  
b. PauliGate defines fixed tensor products of Pauli matrices, while LinearFunction represents arbitrary reversible linear circuits.  
c. LinearFunction is irreversible, while PauliGate is reversible.  
d. Both are non-unitary but provide symbolic representations.  
"""

from qiskit.circuit.library import PauliGate, LinearFunction
import numpy as np

pauli = PauliGate("XZ")
linfunc = LinearFunction(np.eye(2, dtype=int))
print(pauli)
print(linfunc)

# ---------------------------------------------------------------
"""
# Question 8
Which gate provides a **unitary defined directly by a user-specified matrix**?

a. Isometry  
b. UnitaryGate  
c. DiagonalGate  
d. PermutationGate  
"""

from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import random_unitary

U = random_unitary(2)
ugate = UnitaryGate(U)
print(ugate)

# ---------------------------------------------------------------
"""
# Question 9
Which class implements **uniformly controlled Pauli rotations**?

a. UCGate  
b. UCPauliRotGate  
c. MCMTGate  
d. MSGate  
"""

from qiskit.circuit.library import UCPauliRotGate
from math import pi

ucpr = UCPauliRotGate([pi/2, pi/3], "Z")
print(ucpr)

# ---------------------------------------------------------------
"""
# Question 10
What distinguishes the `AndGate` and `OrGate` classes from their circuit counterparts (`AND`, `OR`)?

a. They are implemented as classical logic functions, not quantum gates.  
b. They subclass Gate, allowing abstract compilation and reasoning.  
c. They are backend-specific instructions.  
d. They always require dirty ancillas.  
"""

from qiskit.circuit.library import AndGate, OrGate

and_gate = AndGate(2)
or_gate = OrGate(2)
print(and_gate)
print(or_gate)

# ---------------------------------------------------------------
"""
# Question 11
What is the function of `random_bitwise_xor()`?

a. It generates a random Clifford circuit.  
b. It creates a random BitwiseXorGate instance.  
c. It produces a random measurement mapping.  
d. It permutes Boolean input bits stochastically.  
"""

from qiskit.circuit.library import random_bitwise_xor

xor_gate = random_bitwise_xor(3, seed=42)
print(xor_gate)

# ---------------------------------------------------------------
"""
# Question 12
Which generalized gate performs a **basis transformation** such as the Quantum Fourier Transform?

a. QFTGate  
b. LinearFunction  
c. RVGate  
d. GlobalPhaseGate  
"""

from qiskit.circuit.library import QFTGate

qft = QFTGate(3)
print(qft)

# ---------------------------------------------------------------
"""
Answer Key Summary
------------------
1. b  
2. a  
3. b  
4. b  
5. a  
6. a  
7. b  
8. b  
9. b  
10. b  
11. b  
12. a  
"""
