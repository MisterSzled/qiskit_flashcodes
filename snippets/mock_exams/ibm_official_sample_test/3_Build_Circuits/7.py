"""

7. Given the code fragment below, which of the following code fragments creates a
rotation gate with an angle that has an initially undefined value?

from qiskit.circuit import QuantumCircuit, Parameter, ParameterExpression
qc = QuantumCircuit(1)

a.
theta = 3.14
qc.rx(3.14, 0)

b.
theta = Parameter('theta')
qc.rx(theta, 0)

c.
qc.rx('theta', 0)

d.
qc.rx(ParameterExpression('theta'), 0)

"""

from qiskit.circuit import QuantumCircuit, Parameter, ParameterExpression
from qiskit.visualization import circuit_drawer

# Option A
theta_a = 3.14
qc_a = QuantumCircuit(1)
qc_a.rx(theta_a, 0)

# Option B
theta_b = Parameter('theta')
qc_b = QuantumCircuit(1)
qc_b.rx(theta_b, 0)

# Option C
qc_c = QuantumCircuit(1)
qc_c.rx('theta', 0)  # Will raise an error (invalid argument type)

# Option D
qc_d = QuantumCircuit(1)
try:
        qc_d.rx(ParameterExpression('theta'), 0)
except Exception as e:
        print("Option D error:", e)

# Draw valid circuits
print("\nOption A:")
print(qc_a.draw())

print("\nOption B:")
print(qc_b.draw())

# Option C will not run successfully; Option D also invalid in Qiskit 2.x
"""
SUMMARY:
- Demonstrates four candidate ways of defining a rotation gate.
- Only one defines a *parameterized angle* (symbolic, not numeric).
- Parameter objects enable later binding of values for flexible circuit construction.
"""
