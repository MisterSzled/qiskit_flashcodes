"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Working with Circuit-Level Objects
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
Which function compiles an abstract QuantumCircuit into a hardware-ready, physical circuit compatible with a given backend or target?

a. compile_circuit()
b. transpile()
c. assemble()
d. generate_preset_pass_manager()

# Example:
# from qiskit import QuantumCircuit, transpile
# qc = QuantumCircuit(2)
# qc.cx(0,1)
# transpiled = transpile(qc, backend)
"""
from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(2)
qc.cx(0, 1)
compiled = transpile(qc)
print(type(compiled))

# ---------------------------------------------------------------
"""
# Question 2
Which constructor simulates the effect of a unitary QuantumCircuit on the |00...0⟩ state directly, producing a quantum state representation?

a. Statevector()
b. Operator()
c. AerSimulator()
d. StatevectorSimulator()

# Example:
# from qiskit.quantum_info import Statevector
# psi = Statevector(qc)
"""
from qiskit.quantum_info import Statevector

qc2 = QuantumCircuit(1)
qc2.h(0)
state = Statevector(qc2)
print(state)

# ---------------------------------------------------------------
"""
# Question 3
What is the purpose of the SessionEquivalenceLibrary in Qiskit 2.x?

a. It permanently modifies StandardEquivalenceLibrary.
b. It provides a global-state equivalence database where custom gate mappings can be added.
c. It prevents user-defined equivalence additions for safety.
d. It automatically replaces BasisTranslator in transpilation.

"""
from qiskit.circuit import SessionEquivalenceLibrary, QuantumCircuit, Parameter 
from qiskit.circuit.library import RZGate

theta = Parameter("θ")
alt_circ = QuantumCircuit(1)
alt_circ.rz(theta, 0)
SessionEquivalenceLibrary.add_equivalence(RZGate(theta), alt_circ)

# ---------------------------------------------------------------
"""
# Question 4
Which function creates random, logically equivalent copies of a circuit to suppress coherent errors via stochastic averaging?

a. depolarize_circuit()
b. randomize_paulis()
c. pauli_twirl_2q_gates()
d. twirl_transpile()

# Example:
# from qiskit.circuit import pauli_twirl_2q_gates
# twirled = pauli_twirl_2q_gates(qc)
"""
from qiskit.circuit import pauli_twirl_2q_gates

qc3 = QuantumCircuit(2)
qc3.cx(0,1)
twirled = pauli_twirl_2q_gates(qc3)
print(isinstance(twirled, QuantumCircuit))

# ---------------------------------------------------------------
"""
# Question 5
When using pauli_twirl_2q_gates(), what is the effect of specifying the `num_twirls` argument?

a. It sets the number of random Pauli gates inserted per two-qubit gate.
b. It defines the number of random circuits generated, returned as a list.
c. It controls how many qubits are twirled in parallel.
d. It limits the number of supported gate types.

"""
qc4 = QuantumCircuit(2)
qc4.cz(0,1)
from qiskit.circuit import pauli_twirl_2q_gates
multi = pauli_twirl_2q_gates(qc4, num_twirls=2)
print(isinstance(multi, list))

# ---------------------------------------------------------------
"""
Answer Key Summary

1. b
2. a
3. b
4. c
5. b
"""
