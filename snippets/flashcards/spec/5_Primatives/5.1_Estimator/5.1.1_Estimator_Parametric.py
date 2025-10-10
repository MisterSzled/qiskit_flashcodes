# Flashcard 5.1.1 - EstimatorV2 with Parametric Circuit

import qiskit.circuit.library as qlib
from qiskit.quantum_info import SparsePauliOp
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2
import numpy as np
from qiskit_aer import AerSimulator

# --- Option flag ---
USE_AER = True  # Default = True (run locally on Aer). Set to False for IBM Quantum Runtime.

# --- Step 1: Select backend ---
if USE_AER:
        backend_name = "AerSimulator"
        backend = AerSimulator()
else:
        service = QiskitRuntimeService(channel="ibm_quantum")
        backend = service.least_busy(simulator=False)
        backend_name = backend.name

print("Selected backend:", backend_name)

# Parametric circuit (2 qubits, single layer)
qc = qlib.efficient_su2(2, reps=1)

# Observable: Z⊗Z
observable = SparsePauliOp.from_list([("ZZ", 1)])

# Transpile + align observable
isa_circuit = transpile(qc, backend=backend)
isa_observable = observable.apply_layout(isa_circuit.layout)

# Initialize estimator
estimator = EstimatorV2(backend)

# Define parameter sets (broadcasted automatically)
param_sets = [
        np.random.rand(qc.num_parameters),
        np.random.rand(qc.num_parameters),
]

job = estimator.run([(isa_circuit, isa_observable, param_sets)])
result = job.result()[0]

print("\nExpectation values:", result.data.evs)
print("Metadata:", result.metadata)

"""
SUMMARY:
- Demonstrates parameterized circuits with EstimatorV2.
Steps:
        1. Build parameterized SU2 circuit.
        2. Define observable ZZ.
        3. Transpile + align observable layout.
        4. Provide multiple parameter sets → broadcasted automatically.
        5. Run Estimator, retrieve multiple expectation values.
"""
