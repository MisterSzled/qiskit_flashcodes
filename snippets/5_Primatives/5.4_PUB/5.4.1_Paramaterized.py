# 5.4.1 PUB with Parameters
# Demonstrates PUB structure including parameter bindings.

from qiskit.primitives import Estimator
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.quantum_info import Pauli

# Parametrized circuit
theta = Parameter("θ")
qc = QuantumCircuit(1)
qc.ry(theta, 0)

# Observable
obs = Pauli("Z")

# PUB with parameter binding: (circuit, observable, params)
pub = [(qc, obs, {theta: 3.14/2})]

# Run with Estimator
estimator = Estimator()
result = estimator.run(pub).result()

print("PUB with parameters:", pub)
print("Expectation value with θ=π/2:", result[0].data.evs)

"""
SUMMARY:
- PUBs can include parameter bindings:
  [(circuit, observable, {param: value})]
- Enables reusing a single parametrized circuit with different inputs.
- Central to both Sampler and Estimator workflows.
"""
