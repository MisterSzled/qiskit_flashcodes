# Flashcard 5.0.1 - SamplerV2 with Multiple PUBs (Primitive Unified Blocks)

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False)
sampler = SamplerV2(backend)

# Create two circuits: |+> state and Bell state
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.measure_all()

qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure_all()

# Transpile both to ISA circuits
isa1 = transpile(qc1, backend=backend)
isa2 = transpile(qc2, backend=backend)

# Run multiple PUBs in one call
job = sampler.run([isa1, isa2], shots=200)
print("Job ID:", job.job_id())

results = job.result()

# Iterate through results
for i, pub in enumerate(results):
        print(f"\nPUB {i} results:")
        print("Bitstrings:", pub.data.meas.get_bitstrings()[:5])
        print("Counts:", pub.data.meas.get_counts())

"""
SUMMARY:
- Demonstrates running multiple PUBs (circuits) in one Sampler call.
Steps:
        1. Build two circuits (|+> state and Bell state).
        2. Transpile both → ISA circuits.
        3. Run them in a single `sampler.run` call.
        4. Extract results separately from each PUB.
"""
