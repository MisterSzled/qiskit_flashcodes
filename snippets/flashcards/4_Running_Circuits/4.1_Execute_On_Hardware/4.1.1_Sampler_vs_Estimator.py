# Flashcard: Compare Sampler and Estimator primitives
# Demonstrates practical differences in outputs from Sampler (bitstrings) and Estimator (expectation values)

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Options

# --- Step 1: Define a simple circuit ---
qc = QuantumCircuit(2)
qc.h(0)        # Apply Hadamard to qubit 0
qc.cx(0, 1)    # Entangle qubits
qc.measure_all()  # Measure all qubits

print("Circuit defined:")
print(qc)

# --- Step 2: Connect to Qiskit Runtime ---
service = QiskitRuntimeService(channel="ibm_quantum")

# --- Step 3: Configure runtime options ---
options = Options(shots=1024, memory=True, optimization_level=1)
print(f"Configured runtime options: {options}")

# --- Step 4: Initialize primitives ---
sampler = Sampler(options=options)      # Outputs probability distributions
estimator = Estimator(options=options)  # Outputs expectation values

# --- Step 5: Execute with Sampler ---
sampler_job = sampler.run(circuits=qc)
sampler_result = sampler_job.result()
print("\nSampler output (bitstring probabilities):")
print(sampler_result.quasi_dists[0])  # Print quasi-probabilities for each measured bitstring

# --- Step 6: Execute with Estimator ---
# Define observable: Z ⊗ Z
observable = SparsePauliOp.from_list([("ZZ", 1.0)])
estimator_job = estimator.run(circuits=qc, observables=[observable])
estimator_result = estimator_job.result()
print("\nEstimator output (expectation value of Z⊗Z):")
print(estimator_result.values[0])  # Print expectation value

"""
SUMMARY:
- Demonstrates practical differences between Sampler and Estimator primitives.
- Steps executed:
        1. Define a 2-qubit entangled circuit (Bell state) with measurements.
        2. Connect to Qiskit Runtime service.
        3. Configure runtime options (shots, memory, optimization).
        4. Initialize Sampler (for per-shot bitstring probabilities) and Estimator (for expectation values).
        5. Run the circuit with Sampler and print quasi-distribution over measured bitstrings.
        6. Run the circuit with Estimator for observable Z⊗Z and print the expectation value.
- Key points:
  * Sampler returns probabilistic outcomes of measurements (bitstrings).
  * Estimator returns numerical expectation values for observables.
  * Choice of primitive depends on whether you need per-shot results or processed observables.
"""
