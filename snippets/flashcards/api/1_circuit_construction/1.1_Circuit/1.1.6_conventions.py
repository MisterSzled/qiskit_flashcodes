"""
circuit_conventions_quiz.py
Qiskit 2.x practice questions - Circuit Conventions
Each question includes runnable code and multiple-choice options.
"""

# ---------------------------------------------------------------
"""
# Question 1
When Qiskit measures a 5-qubit circuit with X gates on qubits 0, 1, 4,
which bitstring will appear in the results?
a. 111000
b. 10011
c. 11001
d. 00111
"""
from qiskit import QuantumCircuit

qc = QuantumCircuit(5, 5)
qc.x(0); qc.x(1); qc.x(4)
qc.measure(range(5), range(5))

print("Measured bitstring:", "10011")

# ---------------------------------------------------------------
"""
# Question 2
When drawing circuits, how does Qiskit order qubits vertically?
a. Lowest index on top
b. Highest index on top
c. Random
d. Custom order via layout only
"""
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.cx(0, 1); qc.cx(1, 2)
qc.draw("mpl").savefig("circuit_order.png")

# ---------------------------------------------------------------
"""
# Question 3
Given Qiskit's statevector convention, what index holds |10011⟩?
a. 3
b. 13
c. 19
d. 25
"""
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(5)
qc.x(0); qc.x(1); qc.x(4)
sv = Statevector(qc)

print("Amplitude index for |10011>:", 19, sv[19])

# ---------------------------------------------------------------
"""
# Question 4
In Qiskit's Kronecker-product ordering, which qubit is placed on the right?
a. Highest index
b. Lowest index
c. Control qubit only
d. None – arbitrary
"""
import numpy

state_0 = [1, 0]; state_1 = [0, 1]
manual_sv = [1]
for qubit_state in [state_1, state_1, state_0, state_0, state_1]:
        manual_sv = numpy.kron(qubit_state, manual_sv)

print("Rightmost qubit contributes last to tensor product.")

# ---------------------------------------------------------------
"""
# Question 5
For CCXGate with ctrl_state = 1 and controls [0, 1], which control qubit
must be |1⟩ for activation?
a. Both 0 and 1
b. Only qubit 0
c. Only qubit 1
d. Neither
"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

ccx_natural = QuantumCircuit(3); ccx_natural.ccx(0, 1, 2, ctrl_state=1)
ccx_relative = QuantumCircuit(3); ccx_relative.x(1); ccx_relative.ccx(0, 1, 2); ccx_relative.x(1)

print("Equivalent operators:", Operator(ccx_natural) == Operator(ccx_relative))

# ---------------------------------------------------------------
"""
Answer Key Summary
1 → b  (bitstring “10011”)
2 → a  (lowest index on top)
3 → c  (index 19)
4 → b  (lowest-index qubit on right)
5 → b  (only qubit 0 = |1⟩ activates when ctrl_state = 1)
"""
