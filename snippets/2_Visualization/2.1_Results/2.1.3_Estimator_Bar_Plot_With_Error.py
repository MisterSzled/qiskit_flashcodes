# Flashcard 2.0.3 (Aer version): Plot estimator results with error bars
# Demonstrates:
# - Using Aer EstimatorV2
# - Extracting standard errors from results
# - Adding error bars to matplotlib bar plots

from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit_aer.primitives import EstimatorV2 as Estimator

# Step 1: Build quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(1.5, 0, 1)
print("[INFO] Quantum circuit created.")
print(qc)

# Step 2: Define observables
observables_labels = ["ZZ", "XX", "YZ", "ZY", "XY", "XZ", "ZX"]
observables = [SparsePauliOp(label) for label in observables_labels]

# Step 3: Run Estimator (Aer local simulator)
estimator = Estimator()
job = estimator.run([(qc, observables)])
result = job.result()[0]

# Step 4: Extract results
exp_val = result.data.evs            # Expectation values
standard_error = result.data.stds    # Standard errors
print("[RESULT] Expectation values:", exp_val.flatten())
print("[RESULT] Standard errors:", standard_error.flatten())

# Step 5: Plot results with error bars
_, ax = plt.subplots()
ax.bar(
        observables_labels,
        exp_val.flatten(),
        yerr=standard_error.flatten(),   # Error bars
        capsize=2                        # Small cap lines
)
ax.set_title("Expectation values (with standard errors)")
plt.show()

"""
SUMMARY:
- Demonstrates Aer Estimator with error bars.
- Steps:
        1. Build a 2-qubit circuit with H and CRX.
        2. Define 7 Pauli observables.
        3. Use Aer Estimator to compute expectation values and errors.
        4. Extract evs and stds from the result.
        5. Plot with matplotlib bar chart + error bars.
"""
