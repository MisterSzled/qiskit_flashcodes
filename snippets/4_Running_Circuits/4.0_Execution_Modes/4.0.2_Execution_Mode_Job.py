# Flashcard: Single job execution mode
# Demonstrates submitting a single primitive quantum job

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

# --- Step 1: Connect to IBM Quantum service ---
service = QiskitRuntimeService(channel="ibm_quantum")

# --- Step 2: Prepare a single quantum circuit ---
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

# --- Step 3: Submit as a single job ---
sampler = Sampler(session=None)  # None = job mode
job = sampler.run(qc)

# --- Step 4: Fetch results ---
result = job.result()
print("Single job execution result:", result.quasi_dists)

"""
SUMMARY:
- Demonstrates job execution mode for a single circuit.
- Steps executed:
        1. Connect to IBM Quantum Runtime service.
        2. Prepare one quantum circuit.
        3. Submit circuit as a single job.
        4. Fetch and print result.
- Key points:
  * Simple to use for small experiments.
  * Job might run sooner than batch but less efficient for multiple jobs.
  * Best for single or quick test circuits.
"""
