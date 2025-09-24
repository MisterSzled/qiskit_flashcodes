# Flashcard 5.1.0 - EstimatorV2: Basic Expectation Value

from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False)
print("Selected backend:", backend.name)

# Circuit: prepare |+> state
qc = QuantumCircuit(1)
qc.h(0)

# Observable: Pauli Z
observable = SparsePauliOp("Z", coeffs=[1])

# Transpile
isa_circuit = transpile(qc, backend=backend)
isa_observable = observable.apply_layout(isa_circuit.layout)

# Initialize estimator
estimator = EstimatorV2(backend)

# Run (circuit, observable, param_values)
job = estimator.run([(isa_circuit, isa_observable, [])])
print("Job ID:", job.job_id())

result = job.result()[0]
print("\nExpectation value:", result.data.evs)
print("Metadata:", result.metadata)

"""
SUMMARY:
- Demonstrates using EstimatorV2 to compute expectation values.
Steps:
        1. Build |+> state circuit.
        2. Define observable Z.
        3. Transpile + align observable layout.
        4. Run Estimator.
        5. Retrieve expectation value + metadata.
"""
