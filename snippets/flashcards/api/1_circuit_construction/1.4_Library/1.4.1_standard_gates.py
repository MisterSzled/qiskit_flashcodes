"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Standard Gates (qiskit.circuit.library.standard_gates)
"""

# ---------------------------------------------------------------
"""
# Question 1
Which statement correctly describes the class hierarchy of standard gates in Qiskit 2.x?

a. All standard gates subclass the Instruction class directly.  
b. Standard gates are non-reversible and subclass Operation.  
c. Standard gates are reversible unitary operations that subclass Gate.  
d. Standard gates are backend-specific and subclass TranspileTarget.  
"""

from qiskit.circuit.library import XGate

gate = XGate()
print(isinstance(gate, type(XGate())))
print("All standard gates subclass Gate, which defines reversible unitary operations.")

# ---------------------------------------------------------------
"""
# Question 2
What do the methods `to_matrix()`, `power()`, and `control()` have in common for standard gates?

a. They are available only for measurement and reset operations.  
b. They apply to reversible unitary operations such as Gate subclasses.  
c. They are deprecated and replaced by `decompose()`.  
d. They can only be called after a gate is added to a circuit.  
"""

from qiskit.circuit.library import XGate

gate = XGate()
print(gate.to_matrix())             # X gate
print(gate.power(1/2).to_matrix())  # √X gate
print(gate.control(1).to_matrix())  # CX gate

# ---------------------------------------------------------------
"""
# Question 3
Which function returns a mapping of all standard gate names to their corresponding Qiskit objects?

a. qiskit.circuit.library.get_standard_gate_catalog()  
b. qiskit.circuit.library.get_standard_gate_name_mapping()  
c. qiskit.get_gate_objects()  
d. qiskit.circuit.library.standard_gate_table()  
"""

from qiskit.circuit.library import get_standard_gate_name_mapping

gate_name_map = get_standard_gate_name_mapping()
print(list(gate_name_map.keys())[:5])  # Show first few available gate names

# ---------------------------------------------------------------
"""
# Question 4
What does the object returned for `'cx'` by get_standard_gate_name_mapping() represent?

a. A callable function that constructs controlled gates dynamically.  
b. A singleton CXGate instance representing the controlled-X operation.  
c. A numeric identifier for the CX gate.  
d. A dictionary of parameterized CX definitions.  
"""

cx_object = gate_name_map["cx"]
print(cx_object)
print(type(cx_object))

# ---------------------------------------------------------------
"""
# Question 5
Which of the following gates is a **parametric two-qubit interaction**?

a. CXGate  
b. SwapGate  
c. RZZGate  
d. DCXGate  
"""

from qiskit.circuit.library import RZZGate
from math import pi

gate = RZZGate(pi/3)
print(gate.to_matrix())

# ---------------------------------------------------------------
"""
# Question 6
Which standard gate applies a fixed **global phase** to the circuit and does not take any qubit arguments?

a. PhaseGate  
b. GlobalPhaseGate  
c. RZGate  
d. Barrier  
"""

from qiskit.circuit.library import GlobalPhaseGate
from math import pi

gp = GlobalPhaseGate(pi / 2)
print(gp.to_matrix())

# ---------------------------------------------------------------
"""
# Question 7
Which standard directive acts as a non-unitary instruction meant to be interpreted by the backend or transpiler?

a. Measure  
b. Reset  
c. Barrier  
d. SXGate  
"""

from qiskit.circuit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.barrier()
print(qc)

# ---------------------------------------------------------------
"""
# Question 8
Which standard operation is **non-reversible** and changes the quantum state irreversibly?

a. RXGate  
b. CZGate  
c. Measure  
d. SXdgGate  
"""

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
print(qc)

# ---------------------------------------------------------------
"""
Answer Key Summary
------------------
1. c  
2. b  
3. b  
4. b  
5. c  
6. b  
7. c  
8. c  
"""
