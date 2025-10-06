# 10. Which three of the following are job execution modes in Qiskit Runtime?
#
# a. classical
# b. session
# c. parallel
# d. quantum
# e. batch
# f. single job

from qiskit import QuantumCircuit
from math import pi

# --- Step 1: Create a simple quantum circuit ---
qc = QuantumCircuit(1)
qc.ry(pi / 4, 0)
qc.measure_all()

# --- Step 2: Connect to the Qiskit Runtime service (simulated here) ---
# In a real environment, you would log in using:
# service = QiskitRuntimeService(channel="ibm_quantum")
# For demonstration, we won't actually connect to the cloud.

print("\nSimulating Qiskit Runtime job modes demonstration...")

# --- Step 3: Illustrate Runtime execution modes conceptually ---

# (a) 'classical' — Not a Runtime mode, but local classical simulation could run like this:
print("Mode (a) 'classical': Run locally on a classical simulator (not a Runtime job).")

# (b) 'session' — Run multiple jobs that share backend and data context:
print("Mode (b) 'session': Run a group of related jobs under one Runtime session.")
# Example (mocked, not actually submitting jobs):
# with Session(service=service, backend="ibm_oslo") as session:
#     est = EstimatorV2(session=session)
#     est.run([qc])

# (c) 'parallel' — Running jobs concurrently across multiple backends or sessions:
print("Mode (c) 'parallel': Launch multiple Runtime jobs at once for concurrent execution.")

# (d) 'quantum' — Not an actual mode name, but refers to quantum job type generally.
print("Mode (d) 'quantum': Describes job type, not a specific execution mode.")

# (e) 'batch' — Grouping several jobs submitted together to run sequentially or queued together.
print("Mode (e) 'batch': Submit several circuits as a batch to a backend in one request.")

# (f) 'single job' — The simplest mode: one job executed independently.
print("Mode (f) 'single job': Submit one standalone circuit to run once on a backend.")

# --- Step 4: Summary ---
"""
SUMMARY:
        This example conceptually illustrates Qiskit Runtime execution modes:
        - session: multiple related jobs share the same session and resources.
        - batch: multiple circuits/jobs grouped and sent together.
        - single job: a single standalone execution request.

        Other terms like 'classical', 'parallel', or 'quantum' describe job contexts, 
        not actual Qiskit Runtime mode identifiers.
"""
