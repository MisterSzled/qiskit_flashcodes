"""

Given the code fragment below, which of the following code 
fragments creates a rotation gate with an angle with an initially undefined value?

from qiskit.circuit import QuantumCircuit, Parameter
qc = QuantumCircuit(1)

a. 
phi = 3.14; 
qc.ry(3.14, 0)

b. 
phi = Parameter('phi'); 
qc.ry(phi, 0)

c. 
qc.ry('phi', 0)

d. 
qc.ry(Parameter('phi'), 0)

"""