from qiskit.circuit import Parameter
from qiskit import QuantumCircuit

# Define a symbolic parameter
angle = Parameter("angle")

qc = QuantumCircuit(1)
qc.rx(angle, 0)  # Use parameter in RX gate

print("Circuit with named but currently undefined parameter:")
print(qc)
print("Parameters in circuit:", qc.parameters)

"""
Summary:
- Demonstrates creating parameterized circuits.
- Steps:
        1. Create a symbolic Parameter.
        2. Use it in an RX gate.
        3. Print circuit and check parameters.
"""
