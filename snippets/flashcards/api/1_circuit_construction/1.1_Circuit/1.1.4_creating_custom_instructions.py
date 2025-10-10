"""
IBM Professional Certification Program
Exam C1000-179 (Mock)
Section: Creating Custom Instructions and Gates
Target Version: Qiskit 2.x
"""

# ---------------------------------------------------------------
"""
# Question 1
Which method converts a small QuantumCircuit into a reusable instruction that can be appended to another circuit?

a. QuantumCircuit.compose()
b. QuantumCircuit.to_instruction()
c. QuantumCircuit.define()
d. QuantumCircuit.bind_parameters()

# Example:
# sub_circ = QuantumCircuit(1)
# sub_circ.h(0)
# instr = sub_circ.to_instruction()
# qc.append(instr, [0])
"""
from qiskit import QuantumCircuit

sub = QuantumCircuit(1)
sub.h(0)
qc = QuantumCircuit(1)
qc.append(sub.to_instruction(), [0])
print(qc)

# ---------------------------------------------------------------
"""
# Question 2
When subclassing Gate to define a new parametric gate, what is the primary purpose of implementing the _define() method?

a. To immediately execute the gate on the backend
b. To lazily populate the _definition cache with a QuantumCircuit decomposition
c. To register the gate as a singleton instance
d. To convert the gate to a matrix representation

"""
from qiskit.circuit import Gate, QuantumCircuit

class SimpleGate(Gate):
        def __init__(self, angle):
                super().__init__("simple", 1, [angle])
        def _define(self):
                circ = QuantumCircuit(1)
                circ.rx(self.params[0], 0)
                self._definition = circ
print(SimpleGate(0.5))

# ---------------------------------------------------------------
"""
# Question 3
In custom gate subclasses, which method provides the Numpy array representation used by to_matrix()?

a. __define__()
b. __array__()
c. __matrix__()
d. to_numpy()

"""
import numpy as np, math
from qiskit.circuit import Gate

class DemoGate(Gate):
        def __init__(self, theta):
                super().__init__("demo", 1, [theta])
        def __array__(self, dtype=None, copy=None):
                cos = math.cos(self.params[0]/2)
                sin = math.sin(self.params[0]/2)
                return np.array([[cos, -1j*sin],[-1j*sin, cos]], dtype=dtype)
print(DemoGate(math.pi/2).to_matrix())

# ---------------------------------------------------------------
"""
# Question 4
When defining a custom subclass using SingletonGate, what requirement must be considered during _define() execution?

a. _define() is never called unless invoked manually.
b. _define() is called eagerly after class creation, so only already-defined gates can be used.
c. _define() automatically runs on the first instance call, allowing cyclic imports.
d. _define() only triggers after the gate is appended to a QuantumCircuit.

"""
from qiskit.circuit.singleton import SingletonGate
from qiskit.circuit import QuantumCircuit

class FixedGate(SingletonGate):
        def __init__(self):
                super().__init__("fixed", 1, [])
        def _define(self):
                circ = QuantumCircuit(1)
                circ.x(0)
                self._definition = circ
print(FixedGate().definition)

# ---------------------------------------------------------------
"""
# Question 5
How can a developer register an equivalence between a custom gate and an alternative decomposition for translation?

a. By subclassing BasisTranslator
b. By calling SessionEquivalenceLibrary.add_equivalence()
c. By modifying Gate._definition directly
d. By importing from qiskit.transpiler.library

"""
from qiskit.circuit import QuantumCircuit, Parameter, SessionEquivalenceLibrary
from qiskit.circuit.library import RZXGate

theta = Parameter("θ")
alt = QuantumCircuit(2)
alt.h(0)
alt.cx(1,0)
alt.rz(theta,0)
alt.cx(1,0)
alt.h(0)
SessionEquivalenceLibrary.add_equivalence(RZXGate(theta), alt)
print("Equivalence added for:", RZXGate)

# ---------------------------------------------------------------
"""
Answer Key Summary

1. b
2. b
3. b
4. b
5. b
"""
