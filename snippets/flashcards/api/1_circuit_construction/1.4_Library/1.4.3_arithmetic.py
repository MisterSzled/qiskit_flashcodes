"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Arithmetic (qiskit.circuit.library.arithmetic)
"""

# ---------------------------------------------------------------
"""
# Question 1
Which statement best describes the purpose of an adder circuit in Qiskit's arithmetic module?

a. It performs reversible quantum addition of two n-qubit registers.  
b. It measures two quantum registers and outputs their classical sum.  
c. It performs non-reversible addition using ancilla qubits.  
d. It multiplies two n-qubit registers and stores the result in a new register.  
"""

from qiskit import QuantumCircuit
from qiskit.circuit.library.arithmetic.adders import CDKMRippleCarryAdder

# 3-bit adder requires 8 qubits (a0-a2, b0-b2, carry_in, carry_out)
adder = CDKMRippleCarryAdder(3)
qc = QuantumCircuit(8)

qc.append(adder, range(8))
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 2
What is the function of the MultiplierGate in Qiskit's arithmetic library?

a. It computes the product of two equally sized qubit registers into a new register.  
b. It adds the values of two registers modulo 2ⁿ.  
c. It performs subtraction using ripple-carry logic.  
d. It implements a linear amplitude scaling of the input qubits.  
"""

from qiskit.circuit.library.arithmetic.multipliers import MultiplierGate
from qiskit import QuantumCircuit

mult = MultiplierGate(2)
qc = QuantumCircuit(mult.num_qubits)
qc.append(mult, range(mult.num_qubits))
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 3
What does the LinearAmplitudeFunctionGate class in Qiskit implement?

a. A gate that performs classical addition of binary-encoded integers.  
b. A circuit implementing a (piecewise) linear function on qubit amplitudes.  
c. A polynomial Pauli rotation applied to each amplitude.  
d. A QFT-based method for encoding linear combinations of states.  
"""

from qiskit import QuantumCircuit
from qiskit.circuit.library.arithmetic import LinearAmplitudeFunctionGate

# Define a linear function f(x) = slope * x + offset
# domain and image define normalization intervals
gate = LinearAmplitudeFunctionGate(
        num_state_qubits=2,
        slope=0.5,
        offset=0.25,
        domain=(0, 3),   # x ∈ [0, 3]
        image=(0, 1)     # f(x) ∈ [0, 1]
)

qc = QuantumCircuit(gate.num_qubits)
qc.append(gate, range(gate.num_qubits))
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 4
Which of the following describes a Functional Pauli Rotation?

a. A controlled rotation whose angle depends on a function f(x) of the input qubits.  
b. A linear addition gate using Pauli-X operations.  
c. A non-reversible function applied directly to measurement results.  
d. A Pauli-Z phase estimation routine for QPE circuits.  
"""

from qiskit.circuit.library.arithmetic import LinearPauliRotations
from qiskit import QuantumCircuit

rot = LinearPauliRotations(2)
qc = QuantumCircuit(rot.num_qubits)
qc.append(rot, range(rot.num_qubits))
print(qc.draw())

# ---------------------------------------------------------------
"""
# Question 5
Which of the following correctly describes the IntegerComparatorGate?

a. It computes the sum of two qubit registers.  
b. It performs a ≥ or < comparison between a quantum register and a classical integer.  
c. It implements the exact reciprocal of a register value.  
d. It encodes a quadratic form on binary variables.  
"""

from qiskit.circuit.library.arithmetic import IntegerComparator
from qiskit import QuantumCircuit

comp = IntegerComparator(num_state_qubits=3, value=5)
qc = QuantumCircuit(comp.num_qubits)
qc.append(comp, range(comp.num_qubits))
print(qc.draw())

# ---------------------------------------------------------------
"""
Answer Key Summary
------------------
1. a  
2. a  
3. b  
4. a  
5. b  
"""
