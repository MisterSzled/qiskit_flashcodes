# Flashcard: Batch execution mode
# Demonstrates submitting multiple quantum jobs together for efficiency
# Toggle between Aer simulator and IBM Quantum Runtime with USE_AER

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit_aer.primitives import Sampler as AerSampler

# --- Option flag ---
USE_AER = True  # Set to False to use IBM Quantum Runtime

# --- Step 1: Connect to backend ---
if USE_AER:
        backend_name = "Aer (local simulator)"
        sampler = AerSampler()
else:
        backend_name = "IBM Quantum Runtime"
        service = QiskitRuntimeService(channel="ibm_quantum")
        sampler = Sampler(session=None)  # None = batch mode

print(f"Using backend: {backend_name}")

# --- Step 2: Prepare multiple circuits for batch execution ---
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.measure_all()

qc2 = QuantumCircuit(1)
qc2.x(0)
qc2.measure_all()

batch_circuits = [qc1, qc2]

# --- Step 3: Submit batch jobs ---
job = sampler.run(batch_circuits)

# --- Step 4: Fetch results ---
result = job.result()
print("\nBatch execution results:")
for i, counts in enumerate(result.quasi_dists):
        print(f"  Circuit {i}:", counts)

"""
SUMMARY:
- Demonstrates batch execution mode with a toggle for Aer or IBM Quantum Runtime.
- Steps executed:
        1. Select backend with USE_AER flag.
        2. Prepare multiple circuits.
        3. Submit circuits together in batch mode.
        4. Fetch and print results.
- Key points:
  * Aer is local and fast for prototyping.
  * IBM Quantum Runtime submits to real hardware or managed simulators.
  * Switching is as simple as flipping USE_AER.
"""
