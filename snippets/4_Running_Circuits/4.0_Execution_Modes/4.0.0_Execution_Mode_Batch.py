# Flashcard: Batch execution mode
# Demonstrates submitting multiple quantum jobs together for efficiency

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

# --- Step 1: Connect to IBM Quantum service ---
service = QiskitRuntimeService(channel="ibm_quantum")

# --- Step 2: Prepare multiple circuits for batch execution ---
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.measure_all()

qc2 = QuantumCircuit(1)
qc2.x(0)
qc2.measure_all()

batch_circuits = [qc1, qc2]

# --- Step 3: Submit batch jobs ---
sampler = Sampler(session=None)  # None = batch mode (no dedicated session)
job = sampler.run(batch_circuits)

# --- Step 4: Fetch results ---
result = job.result()
print("Batch execution results:")
for i, counts in enumerate(result.quasi_dists):
        print(f"Circuit {i}:", counts)

"""
SUMMARY:
- Demonstrates batch execution mode for multiple jobs.
- Steps executed:
        1. Connect to IBM Quantum Runtime service.
        2. Prepare multiple quantum circuits.
        3. Submit all circuits together in batch mode.
        4. Fetch and print results from each circuit.
- Key points:
  * Jobs are scheduled together; minimal queuing time.
  * Parallel classical computation reduces total runtime.
  * Useful for independent but related jobs, e.g., error mitigation comparisons.
"""
