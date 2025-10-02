from qiskit.circuit import Parameter
from qiskit import QuantumCircuit

# Define paramater called 'angle'
angle = Parameter("angle")

qc = QuantumCircuit(1)
qc.rx(angle, 0)

# Create variations with assigned parameter values
circuits = [qc.assign_parameters({angle: v}) for v in range(3)]

for idx, c in enumerate(circuits):
        print(f"Circuit with angle = {idx}:")
        print(c)

"""
Summary:
- Demonstrates assigning values to parameters.
- Steps:
        1. Define parameterized circuit with RX(angle).
        2. Assign multiple values using assign_parameters.
        3. Print out resulting circuits.
"""
