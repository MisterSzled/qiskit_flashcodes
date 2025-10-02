# Flashcard 5.0.1 - SamplerV2 with Multiple PUBs (Primitive Unified Blocks)
# Toggle between Aer simulator and IBM Quantum Runtime with USE_AER

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit_aer import AerSimulator

# --- Option flag ---
USE_AER = True  # Default = True (local Aer). Set to False for IBM Quantum Runtime.

# --- Step 1: Select backend ---
if USE_AER:
        backend_name = "AerSimulator"
        backend = AerSimulator()
else:
        service = QiskitRuntimeService(channel="ibm_quantum")
        backend = service.least_busy(simulator=False)
        backend_name = backend.name

print("Selected backend:", backend_name)

# --- Step 2: Create circuits ---
# |+> state
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.measure_all()

# Bell state
qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure_all()

# --- Step 3: Transpile to ISA circuits ---
isa1 = transpile(qc1, backend=backend)
isa2 = transpile(qc2, backend=backend)

# --- Step 4: Initialize SamplerV2 ---
sampler = SamplerV2(backend)

# --- Step 5: Run multiple PUBs in one call ---
job = sampler.run([isa1, isa2], shots=200)
print("Job ID:", job.job_id())

# --- Step 6: Collect results ---
results = job.result()

# --- Step 7: Iterate through PUB results ---
for i, pub in enumerate(results):
        print(f"\nPUB {i} results:")
        print("Bitstrings:", pub.data.meas.get_bitstrings()[:5])
        print("Counts:", pub.data.meas.get_counts())

"""
SUMMARY:
- Demonstrates running multiple PUBs (circuits) in one SamplerV2 call.
Steps:
        1. Select backend via USE_AER flag.
        2. Build two circuits (|+> state and Bell state).
        3. Transpile both to ISA circuits.
        4. Run them in a single sampler call.
        5. Extract results from each PUB separately.
- Aer = local, fast testing (default).
- IBM Runtime = real backend or managed simulators.
"""
