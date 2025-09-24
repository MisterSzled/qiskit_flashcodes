# Flashcard 5.0.3 - Bypassing runtime error mitigations with Sampler

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False)

# Explicitly disable error mitigation features
sampler = SamplerV2(
        backend,
        resilience={"measure_mitigation": False},  # disable measurement mitigation
        options={"resilience_level": 0},          # turn off runtime auto-mitigation
)

# Simple Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

isa_circuit = transpile(qc, backend=backend)

# Run sampler without runtime mitigation
job = sampler.run([isa_circuit], shots=100)
result = job.result()
pub_result = result[0]

print("Raw counts (no mitigation):", pub_result.data.meas.get_counts())

"""
SUMMARY:
- Demonstrates bypassing runtime error mitigation in Sampler.
Steps:
        1. Initialize Sampler with resilience_level=0.
        2. Build a Bell state circuit.
        3. Run Sampler with mitigation disabled.
        4. Show raw hardware counts (unmitigated data).
"""
