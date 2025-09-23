# Flashcard: Execute circuits on Qiskit Runtime hardware
# Demonstrates running a quantum circuit on real hardware using Sampler or Estimator primitives
# Includes logging of execution mode, results, and error mitigation options

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Options

# --- Step 1: Define a simple circuit ---
qc = QuantumCircuit(2)
qc.h(0)        # Apply Hadamard gate to qubit 0
qc.cx(0, 1)    # Apply CNOT gate to create entanglement
qc.measure_all()  # Measure all qubits

print("Circuit defined:")
print(qc)

# --- Step 2: Connect to Qiskit Runtime ---
# Ensure you have IBM Quantum API credentials configured
service = QiskitRuntimeService(channel="ibm_quantum")

# --- Step 3: Choose execution mode ---
execution_mode = "Batch"  # Options: "Batch" or "Session"
print(f"Selected execution mode: {execution_mode}")

# --- Step 4: Configure runtime options ---
# Example: configure error mitigation (mock example; actual usage depends on backend support)
runtime_options = Options(
        shots=1024,
        memory=True,
        optimization_level=1,   # Use light transpiler optimization
        # error_mitigation=True  # Uncomment if backend supports
)
print(f"Configured runtime options: {runtime_options}")

# --- Step 5: Initialize a primitive ---
# Sampler outputs per-shot measurements (bitstrings)
sampler = Sampler(session=None, options=runtime_options)

# Estimator outputs expectation values for observables
# estimator = Estimator(session=None, options=runtime_options)

# --- Step 6: Execute the circuit ---
job = sampler.run(circuits=qc)
result = job.result()  # Blocks until execution finishes
print("Execution completed. Sample output:")
print(result.quasi_dists[0])  # Print probability distribution of measured bitstrings

"""
SUMMARY:
- Demonstrates executing a quantum circuit on target hardware using Qiskit Runtime.
- Steps executed:
        1. Define a simple two-qubit entangled circuit with measurements.
        2. Connect to Qiskit Runtime service (requires IBM Quantum API credentials).
        3. Choose execution mode: Batch (parallel jobs) or Session (iterative/dedicated).
        4. Configure runtime options, e.g., shots, memory, optimization level, error mitigation.
        5. Initialize a primitive (Sampler for bitstrings, Estimator for expectation values).
        6. Run the circuit on hardware and retrieve results.
- Key points:
  * Sampler gives per-shot measurement results.
  * Estimator gives expectation values for observables.
  * Batch mode reduces queuing for multiple jobs; Session mode allows iterative feedback.
  * Error suppression and mitigation can be configured via runtime options.
"""
