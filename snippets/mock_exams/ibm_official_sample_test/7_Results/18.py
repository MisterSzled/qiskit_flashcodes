# 18. Which statement describes the purpose of a Qiskit Runtime session?
# a. Automatically generate quantum algorithms based on user input
# b. Visualise the results of quantum experiments in real time
# c. Group a collection of calls to the quantum computer
# d. Compile and optimise quantum circuits for different backends
#
# This example conceptually shows how sessions allow multiple circuit executions
# to share context (like a dedicated runtime environment).

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# --- Step 1: Define simple circuits ---
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.measure_all()

qc2 = QuantumCircuit(1)
qc2.x(0)
qc2.measure_all()

# --- Step 2: Conceptual demonstration of a "session" ---
# Note: We'll simulate a session locally using Aer
simulator = AerSimulator()

# Normally, a session groups multiple jobs on IBM backends
# Here, we just run multiple circuits sequentially to demonstrate the idea
results = []
for i, qc in enumerate([qc1, qc2], start=1):
        job = simulator.run(qc, shots=1000)
        result = job.result()
        counts = result.get_counts()
        results.append(counts)
        print(f"Result of circuit {i}: {counts}")

"""
SUMMARY:
- Demonstrates the concept of a Qiskit Runtime session.
- Steps:
        1. Prepare multiple circuits.
        2. Run them sequentially within a shared context (simulated locally).
        3. Collect results for each circuit.
- Key point:
    * A session allows grouping multiple calls to the quantum computer,
        reducing overhead and enabling iterative workflows.
- Correct answer: (c) Group a collection of calls to the quantum computer
"""
