# Flashcard 5.3.0 - Simulating Backends with Qiskit AER

from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
from qiskit.primitives import BackendSamplerV2, BackendEstimatorV2
from qiskit.quantum_info import SparsePauliOp

# 1. Create local simulator backend
sim = AerSimulator()
print("Simulator backend:", sim)

# 2. Build Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# 3. Transpile for simulator
isa_circuit = transpile(qc, backend=sim)

# 4. Sampler with simulator
sampler = BackendSamplerV2(sim)
job = sampler.run([isa_circuit], shots=100)
print("\nSampler results:", job.result()[0].data.meas.get_counts())

# 5. Estimator with simulator (no measurement needed)
qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0, 1)

observable = SparsePauliOp.from_list([("ZZ", 1)])
isa_circuit2 = transpile(qc2, backend=sim)

estimator = BackendEstimatorV2(sim)
job2 = estimator.run([(isa_circuit2, observable, [])])
print("\nEstimator expectation value:", job2.result()[0].data.evs)

"""
SUMMARY:
- Demonstrates using Qiskit AER simulator as backend for primitives.
Steps:
        1. Create AerSimulator.
        2. Build Bell state circuit with measurements → Sampler.
        3. Run and get counts.
        4. Build Bell state circuit without measurement → Estimator.
        5. Run and get expectation value.
"""
