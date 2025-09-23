# 4.2.5 Sampler Run
# Demonstrates building and running the Sampler primitive.

import numpy as np
from qiskit.circuit.library import efficient_su2
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler import generate_preset_pass_manager

# Setup
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)

# Build parametrized circuit
circuit = efficient_su2(127, entanglement="linear")
circuit.measure_all()
param_values = np.random.rand(circuit.num_parameters)

# Transpile to ISA
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pm.run(circuit)
print(">>> ISA op counts:", isa_circuit.count_ops())

# Initialize Sampler
sampler = Sampler(mode=backend)

# Run job
job = sampler.run([(isa_circuit, param_values)])
print(">>> Job ID:", job.job_id())
print(">>> Job Status:", job.status())

# Collect results
result = job.result()
pub_result = result[0]
print(">>> First 5 measurement outcomes:", pub_result.data.meas.get_bitstrings()[:5])

"""
SUMMARY:
- Builds and runs a Sampler job.
- Steps:
        1. Select backend and build EfficientSU2 circuit with measurement.
        2. Assign random parameter values.
        3. Transpile to ISA form.
        4. Initialize Sampler in backend mode.
        5. Run Sampler and print measurement samples.
"""
