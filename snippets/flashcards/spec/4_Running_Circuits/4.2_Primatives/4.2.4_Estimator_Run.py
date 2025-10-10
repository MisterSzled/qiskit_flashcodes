# 4.2.4 Estimator Run
# Demonstrates running the Estimator primitive and retrieving expectation values.

from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import qaoa_ansatz

# Setup service and backend
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)

# Build observable and circuit
observable = SparsePauliOp.from_sparse_list([("ZZ", [0, 1], 1.0)], num_qubits=backend.num_qubits)
circuit = qaoa_ansatz(observable, reps=1)
param_values = [0.1, 0.2]

# Transpile
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pm.run(circuit)
isa_observable = observable.apply_layout(isa_circuit.layout)

# Initialize Estimator
estimator = Estimator(mode=backend)

# Run job
job = estimator.run([(isa_circuit, isa_observable, param_values)])
print(">>> Job ID:", job.job_id())
print(">>> Job Status:", job.status())

# Collect results
result = job.result()
print(">>> Expectation value:", result[0].data.evs)
print(">>> Metadata:", result[0].metadata)

"""
SUMMARY:
- Runs Estimator and retrieves results.
- Steps:
        1. Select backend and build simple observable/circuit.
        2. Transpile to ISA form.
        3. Initialize Estimator in backend mode.
        4. Run estimator with (circuit, observable, parameters).
        5. Print job ID, status, expectation values, and metadata.
"""
