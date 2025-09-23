# Flashcard: Session execution mode
# Demonstrates dedicated access to the QPU for iterative workloads

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

# --- Step 1: Connect to IBM Quantum service ---
service = QiskitRuntimeService(channel="ibm_quantum")

# --- Step 2: Start a session for dedicated access ---
with Session(service=service, backend="ibmq_qasm_simulator") as session:
        sampler = Sampler(session=session)

        # --- Step 3: Prepare iterative circuits ---
        qc = QuantumCircuit(1)
        qc.h(0)
        qc.measure_all()

        # --- Step 4: Submit job multiple times in same session ---
        print("Running iterative jobs in session mode...")
        for i in range(3):
                job = sampler.run(qc)
                result = job.result()
                print(f"Iteration {i} results:", result.quasi_dists)

"""
SUMMARY:
- Demonstrates session execution mode for iterative workloads.
- Steps executed:
        1. Connect to IBM Quantum Runtime service.
        2. Open a session to get exclusive backend access.
        3. Prepare a quantum circuit.
        4. Submit and run multiple jobs iteratively within the session.
        5. Print results for each iteration.
- Key points:
  * Session mode avoids repeated queuing between jobs.
  * Useful for variational algorithms or experiments requiring iterative feedback.
  * More expensive than batch mode but provides dedicated access.
"""
