# Flashcard 5.0.2 - Working with DataBin and BitArray results
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

# --- Step 2: Create simple |+> state circuit ---
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

# --- Step 3: Transpile circuit ---
isa_circuit = transpile(qc, backend=backend)

# --- Step 4: Initialize SamplerV2 ---
sampler = SamplerV2(backend)

# --- Step 5: Run sampler ---
job = sampler.run([isa_circuit], shots=50)
result = job.result()
pub_result = result[0]

# --- Step 6: Access DataBin → BitArray ---
bit_array = pub_result.data.meas
print("Raw BitArray:", bit_array)
print("First 10 bitstrings:", bit_array.get_bitstrings()[:10])
print("Counts:", bit_array.get_counts())

"""
SUMMARY:
- Demonstrates how SamplerV2 results are stored in DataBin objects.
- BitArray provides structured access to measurement data.
Steps:
        1. Select backend via USE_AER flag.
        2. Build a simple |+> circuit.
        3. Run with SamplerV2.
        4. Extract DataBin result.
        5. Convert to bitstrings, counts, numpy array.
- Aer = fast, local testing (default).
- IBM Runtime = real backends or managed simulators.
"""
