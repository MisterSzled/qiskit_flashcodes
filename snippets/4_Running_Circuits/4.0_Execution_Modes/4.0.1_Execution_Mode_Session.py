# Flashcard: Session execution mode
# Demonstrates dedicated access to the QPU for iterative workloads
# Toggle between Aer simulator and IBM Quantum Runtime with USE_AER

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
from qiskit_aer.primitives import Sampler as AerSampler

# --- Option flag ---
USE_AER = True  # Set to False to use IBM Quantum Runtime

# --- Step 1: Connect to backend ---
if USE_AER:
        backend_name = "Aer (local simulator)"
        sampler = AerSampler()
        print(f"Using backend: {backend_name}")

        # --- Step 2 (Aer): No session concept, just reuse sampler ---
        qc = QuantumCircuit(1)
        qc.h(0)
        qc.measure_all()

        print("Running iterative jobs (simulated session with Aer)...")
        for i in range(3):
                job = sampler.run(qc)
                result = job.result()
                print(f"Iteration {i} results:", result.quasi_dists)

else:
        backend_name = "IBM Quantum Runtime"
        service = QiskitRuntimeService(channel="ibm_quantum")
        print(f"Using backend: {backend_name}")

        # --- Step 2 (Runtime): Start a session for dedicated access ---
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
- Demonstrates session-style execution with a toggle for Aer or IBM Quantum Runtime.
- Steps executed:
        1. Select backend with USE_AER flag.
        2. Prepare a quantum circuit.
        3. Submit and run multiple jobs iteratively.
        4. Fetch and print results each iteration.
- Key points:
  * Aer: No true session, but loop mimics iterative runs.
  * IBM Runtime: Session mode gives dedicated backend access and avoids queuing.
  * Useful for variational algorithms and feedback-based workloads.
"""
