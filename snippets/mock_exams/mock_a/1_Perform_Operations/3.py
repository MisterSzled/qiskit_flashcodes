"""
3. Given the following code fragment, 
what is the approximate probability that a measurement would result in a bit value of 1?

from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(1)
qc.reset(0)
qc.ry(np.pi/4, 0)
qc.measure_all()

a. 0.8536
b. 1.0
c. 0.1464
d. 0.5
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

# Build circuit
qc = QuantumCircuit(1)
qc.reset(0)
qc.ry(np.pi / 4, 0)
qc.measure_all()

# Simulate
backend = AerSimulator()
isa_circuit = transpile(qc, backend)
job = backend.run(isa_circuit, shots=5000)
result = job.result()
counts = result.get_counts()

print("Measurement counts:", counts)

# Compute probability of measuring '1'
p1 = counts.get("1", 0) / 5000
print("Approximate probability of measuring '1':", p1)