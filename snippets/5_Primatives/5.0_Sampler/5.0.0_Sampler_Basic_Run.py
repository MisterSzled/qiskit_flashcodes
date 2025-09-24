# Flashcard 5.0.0 - SamplerV2: Basic Execution on IBM Runtime

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

# 1. Load IBM Quantum service (requires IBM account setup beforehand)
service = QiskitRuntimeService(channel="ibm_quantum")

# 2. Select backend (replace with one from your account)
backend = service.least_busy(simulator=False)
print("Selected backend:", backend.name)

# 3. Create Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print("\nOriginal circuit:\n", qc)

# 4. Transpile to backend-native gate set (ISA circuit)
isa_circuit = transpile(qc, backend=backend)
print("\nISA circuit:\n", isa_circuit)

# 5. Initialize SamplerV2
sampler = SamplerV2(backend)

# 6. Run PUB (just one circuit)
job = sampler.run([isa_circuit], shots=100)
print("\nJob submitted:", job.job_id())

# 7. Collect results
result = job.result()
pub_result = result[0]

# 8. Extract measurement outcomes
bit_array = pub_result.data.meas
print("\nBitstrings:", bit_array.get_bitstrings()[:10])
print("Counts:", bit_array.get_counts())

"""
SUMMARY:
- Demonstrates running a Bell state with SamplerV2.
Steps:
        1. Connect to IBM service and choose backend.
        2. Build Bell circuit + measurements.
        3. Transpile to ISA.
        4. Run with SamplerV2.
        5. Collect results via DataBin (BitArray).
        6. Convert to bitstrings/counts.
"""
