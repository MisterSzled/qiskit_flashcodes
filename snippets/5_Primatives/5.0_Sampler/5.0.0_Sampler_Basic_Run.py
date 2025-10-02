# Flashcard 5.0.0 - SamplerV2: Basic Execution (Aer vs IBM Runtime)

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
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

# --- Step 2: Create Bell state circuit ---
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print("\nOriginal circuit:\n", qc)

# --- Step 3: Transpile to backend-native gate set (ISA circuit) ---
isa_circuit = transpile(qc, backend=backend)
print("\nISA circuit:\n", isa_circuit)

# --- Step 4: Initialize SamplerV2 ---
sampler = SamplerV2(backend)

# --- Step 5: Run PUB (just one circuit) ---
job = sampler.run([isa_circuit], shots=100)
print("\nJob submitted:", job.job_id())

# --- Step 6: Collect results ---
result = job.result()
pub_result = result[0]

# --- Step 7: Extract measurement outcomes ---
bit_array = pub_result.data.meas
print("\nBitstrings:", bit_array.get_bitstrings()[:10])
print("Counts:", bit_array.get_counts())

"""
SUMMARY:
- Demonstrates running a Bell state with SamplerV2.
Steps:
        1. Choose backend via USE_AER flag.
        2. Build Bell circuit with measurements.
        3. Transpile to backend ISA.
        4. Run with SamplerV2.
        5. Collect results via DataBin (BitArray).
        6. Convert to bitstrings and counts.
- Aer = fast, local testing (default).
- IBM Runtime = real backend or managed simulators.
"""
