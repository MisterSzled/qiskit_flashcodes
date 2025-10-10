"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Qiskit 2.x Circuit Representation and Advanced Features
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
Which statement best describes the purpose of the QuantumCircuit class in Qiskit 2.x?

a. QuantumCircuit is only for visualizing circuits and cannot be executed.
b. QuantumCircuit stores qubits, classical bits, parameters, and instructions for execution.
c. QuantumCircuit is an internal class used only by the transpiler.
d. QuantumCircuit automatically schedules pulses for QPU execution.

"""
from qiskit import QuantumCircuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0,1)
print(qc)

# ---------------------------------------------------------------
"""
# Question 2
Regarding Qubit and Clbit in Qiskit 2.x, which is correct?

a. Qubit and Clbit can be directly instantiated and compared between circuits.
b. Clbit can hold quantum data during execution.
c. Qubit is mutable and can change type during runtime.
d. Qubit() requires a register parent at instantiation.

"""
from qiskit.circuit import Qubit, Clbit
q = Qubit()
c = Clbit()
print(q == q, c == c)

# ---------------------------------------------------------------
"""
# Question 3
Which statement about Registers in Qiskit is accurate?

a. Registers store values but cannot be named.
b. Registers provide behavioral differences for hardware execution.
c. Registers group multiple bits of the same type and can be named for visualization.
d. Registers cannot be used to initialize multiple bits at once.

"""
from qiskit.circuit import QuantumRegister, ClassicalRegister
qreg = QuantumRegister(3, 'qreg')
creg = ClassicalRegister(3, 'creg')
print(qreg, creg)

# ---------------------------------------------------------------
"""
# Question 4
What is the purpose of CircuitInstruction objects in Qiskit 2.x?

a. To execute circuits on hardware directly.
b. To provide a minimal interface containing operations and operands within a circuit.
c. To allow arbitrary mutation of instructions already in a QuantumCircuit.
d. To manage classical variables during execution.

"""
from qiskit import QuantumCircuit
qc = QuantumCircuit(1,1)
instr = qc.h(0)
print(type(instr))

# ---------------------------------------------------------------
"""
# Question 5
Which statement accurately describes the Gate class in Qiskit 2.x?

a. Gate instances are always non-unitary and cannot be decomposed.
b. Gate inherits from Instruction and represents unitary operations with to_matrix() and control() methods.
c. Gate cannot be used as part of custom parametric instructions.
d. Gate can act on classical bits.

"""
from qiskit.circuit import Gate, QuantumRegister, QuantumCircuit
qreg = QuantumRegister(1)
qc = QuantumCircuit(qreg)
my_gate = Gate("my_gate", 1, [])
qc.append(my_gate, [qreg[0]])
print(qc)

# ---------------------------------------------------------------
"""
# Question 6
Which instruction is used to reset a qubit to the |0⟩ state?

a. Delay
b. Measure
c. Reset
d. Barrier

"""
from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.reset(0)
print(qc)

# ---------------------------------------------------------------
"""
# Question 7
Which Qiskit class is used to represent compile-time symbolic parameters?

a. expr.Var
b. Parameter and ParameterExpression
c. CircuitInstruction
d. ControlledGate

"""
from qiskit.circuit import QuantumCircuit, Parameter
theta = Parameter('θ')
qc = QuantumCircuit(1)
qc.rx(theta, 0)
print(qc)

# ---------------------------------------------------------------
"""
# Question 8
Which of the following best describes control flow operations in Qiskit 2.x?

a. ControlFlowOps are purely for documentation purposes and cannot affect execution.
b. ControlFlowOps encapsulate subcircuits with conditional execution, loops, and branching.
c. ControlFlowOps replace the need for classical registers entirely.
d. ControlFlowOps can only contain measurement instructions.

"""
from qiskit import QuantumCircuit
from qiskit.circuit import get_control_flow_name_mapping
ctrl_map = get_control_flow_name_mapping()
print(ctrl_map["if_else"])

# ---------------------------------------------------------------
"""
# Question 9
Which statement about instruction-local annotations in Qiskit 2.x is correct?

a. All instructions can be annotated with arbitrary user-defined annotations.
b. Only BoxOp instructions currently support instruction-local annotations.
c. Annotations are automatically executed on hardware.
d. Annotations are deprecated and should not be used.

"""
from qiskit.circuit import QuantumCircuit
qc = QuantumCircuit(1)
with qc.box():
        qc.h(0)
print(qc)

# ---------------------------------------------------------------
"""
# Question 10
What is the purpose of delayed-resolution scheduling in Qiskit 2.x?

a. To automatically assign parameter values to gates.
b. To control relative scheduling of pulses or operations with flexible “stretch” durations.
c. To optimize gate commutation and cancellation automatically.
d. To convert all quantum operations to classical instructions.

"""
from qiskit import QuantumCircuit
from qiskit.circuit.classical import expr
qc = QuantumCircuit(3,3)
a = qc.add_stretch("a")
b = qc.add_stretch("b")
qc.delay(b, 0)
print(qc)

# ---------------------------------------------------------------
"""
Answer Key Summary

1. b
2. a
3. c
4. b
5. b
6. c
7. b
8. b
9. b
10. b

"""
