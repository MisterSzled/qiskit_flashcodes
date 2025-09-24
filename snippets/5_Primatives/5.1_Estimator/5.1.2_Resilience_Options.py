# Flashcard 5.1.2 - EstimatorV2 with Resilience Options

from qiskit.circuit.library import RealAmplitudes
from qiskit.quantum_info import SparsePauliOp
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False)

# Build a simple variational ansatz
qc = RealAmplitudes(num_qubits=2, reps=1)

# Observable: Z⊗Z
observable = SparsePauliOp.from_list([("ZZ", 1.0)])

# Transpile + align observable layout
isa_circuit = transpile(qc, backend=backend)
isa_observable = observable.apply_layout(isa_circuit.layout)

# Initialize estimator with custom options
estimator = EstimatorV2(
        backend,
        resilience={"measure_mitigation": True},  # enable measurement error mitigation
        options={"resilience_level": 1},          # higher levels = stronger mitigation
)

# Run with a single random parameter set
import numpy as np
params = np.random.rand(qc.num_parameters)

job = estimator.run([(isa_circuit, isa_observable, [params])])
result = job.result()[0]

print("\nExpectation value with mitigation:", result.data.evs)
print("Metadata:", result.metadata)

"""
SUMMARY:
- Demonstrates setting resilience options in EstimatorV2.
Steps:
        1. Build simple variational circuit (RealAmplitudes).
        2. Define observable ZZ and align layout.
        3. Initialize Estimator with resilience_level and mitigation.
        4. Run on backend with random parameters.
        5. Retrieve mitigated expectation values and metadata.
"""
