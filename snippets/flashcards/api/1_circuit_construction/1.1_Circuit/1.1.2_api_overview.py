"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: API Overview of qiskit.circuit
"""

# ---------------------------------------------------------------
"""
# Question 1
In the Qiskit 2.x circuit API, what is the principal class used to represent a complete quantum program structure?

a. CircuitInstruction  
b. QuantumRegister  
c. QuantumCircuit  
d. InstructionSet  
"""

from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure(1, 1)
print(qc)

# ---------------------------------------------------------------
"""
# Question 2
Which of the following correctly describes the relationship between `Operation`, `Instruction`, and `Gate` in Qiskit 2.x?

a. `Instruction` is a subclass of `Operation` that adds hardware execution semantics, and `Gate` adds unitarity.  
b. `Operation` is a subclass of `Instruction` that adds physical coupling rules.  
c. `Gate` is a superclass of `Instruction` representing symbolic transformations.  
d. `Instruction` and `Gate` are unrelated and belong to different modules.  
"""

from qiskit.circuit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)  # X is a Gate subclass of Instruction, itself subclass of Operation
print(qc)

# ---------------------------------------------------------------
"""
# Question 3
Which `ControlFlowOp` subclass would be used to repeatedly execute a subcircuit until a certain condition becomes false?

a. ForLoopOp  
b. BoxOp  
c. WhileLoopOp  
d. ContinueLoopOp  
"""

from qiskit import QuantumCircuit
from qiskit.circuit.controlflow import WhileLoopOp

# Add 1 quantum and 1 classical bit
qc = QuantumCircuit(1, 1)

# Define a simple loop body
loop_body = QuantumCircuit(1)
loop_body.x(0)

# Define while-loop control using qc.clbits[0]
condition = (qc.clbits[0], True)
loop = WhileLoopOp(condition, loop_body)

print("Created control flow operation:", type(loop).__name__)


# ---------------------------------------------------------------
"""
# Question 4
What type of object does the `EquivalenceLibrary` represent in Qiskit's circuit compilation workflow?

a. A dynamic scheduler for classical control flow  
b. A collection of decomposition relations between gates and circuits  
c. A registry of hardware backends and basis gates  
d. A container for real-time classical variables and expressions  
"""

from qiskit.circuit.equivalence import EquivalenceLibrary
from qiskit.circuit.library import HGate

qc_a = QuantumCircuit(1)
qc_a.h(0)

elib = EquivalenceLibrary()
elib.add_equivalence(HGate(), qc_a)

# ---------------------------------------------------------------
"""
# Question 5
What is the correct description of the `ParameterVector` class in the Qiskit 2.x circuit API?

a. It is a runtime classical register of integer values.  
b. It is a symbolic vector grouping multiple compile-time `Parameter` objects.  
c. It is a mutable container for storing `Var` objects.  
d. It is a subclass of `Expr` used for real-time evaluation on hardware.  
"""

from qiskit.circuit import ParameterVector

theta = ParameterVector('theta', 3)
print("ParameterVector elements:", list(theta))

# ----------
"""
Answer Key Summary
------------------
1. c  
2. a  
3. c  
4. b  
5. b  
"""