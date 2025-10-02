# Flashcard 2.0.2: Plot estimator results using Matplotlib (Aer version)
# Demonstrates:
# - Using the Aer Estimator primitive
# - Calculating expectation values for multiple observables
# - Visualizing results with matplotlib bar plots

import numpy as np
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit_aer.primitives import EstimatorV2  # Aer Estimator (local simulator)

# Step 1: Build a small quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(1.5, 0, 1)   # Controlled rotation around X-axis
print("[INFO] Quantum circuit created.")

print(qc)

# Step 2: Define observables
observables_labels = ["ZZ", "XX", "YZ", "ZY", "XY", "XZ", "ZX"]
observables = [SparsePauliOp(label) for label in observables_labels]

# Step 3: Initialize Aer Estimator
estimator = EstimatorV2()

# Step 4: Reshape observables for Estimator input
reshaped_ops = np.fromiter(observables, dtype=object).reshape((7, 1))

# Step 5: Run Estimator job on local simulator
print("[INFO] Running Estimator job...")
job = estimator.run([(qc, reshaped_ops)])
result = job.result()[0]
exp_val = result.data.evs
print("[RESULT]", result)

# Step 6: Plot expectation values
plt.bar(observables_labels, exp_val.flatten())
plt.title("Expectation values of observables (Aer)")
plt.ylabel("Expectation value")
plt.xlabel("Observable")
plt.show()

plt.savefig("bar_plot.png")

"""
SUMMARY:
- Demonstrates plotting of Estimator results manually using matplotlib with Aer.
- Steps:
        1. Build a simple 2-qubit circuit.
        2. Define 7 different observables (Pauli operators).
        3. Initialize Aer Estimator (local simulator).
        4. Reshape observables for Estimator input.
        5. Run Estimator job and extract expectation values.
        6. Plot results as a bar chart with matplotlib.
"""
