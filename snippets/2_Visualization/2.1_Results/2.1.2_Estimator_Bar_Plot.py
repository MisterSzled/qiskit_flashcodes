# Flashcard 2.0.2: Plot estimator results using Matplotlib
# Demonstrates:
# - Using the Estimator primitive
# - Calculating expectation values for multiple observables
# - Visualizing results with matplotlib bar plots

import numpy as np
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.transpiler import generate_preset_pass_manager

# Step 1: Build a small quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(1.5, 0, 1)   # Controlled rotation around X-axis
print("[INFO] Quantum circuit created.")

# Step 2: Define observables
observables_labels = ["ZZ", "XX", "YZ", "ZY", "XY", "XZ", "ZX"]
observables = [SparsePauliOp(label) for label in observables_labels]

# Step 3: Setup service and backend
service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True)

# Step 4: Compile circuit for backend layout
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

# Apply backend layout to observables
isa_observables = [op.apply_layout(isa_circuit.layout) for op in observables]

# Step 5: Reshape observables for Estimator
reshaped_ops = np.fromiter(isa_observables, dtype=object).reshape((7, 1))

# Step 6: Run Estimator job
estimator = Estimator(backend)
job = estimator.run([(isa_circuit, reshaped_ops)])
result = job.result()[0]
exp_val = result.data.evs
print("[RESULT]", result)

# Step 7: Plot expectation values
plt.bar(observables_labels, exp_val.flatten())
plt.title("Expectation values of observables")
plt.show()

"""
SUMMARY:
- Demonstrates plotting of Estimator results manually using matplotlib.
- Steps:
        1. Build a simple 2-qubit circuit.
        2. Define 7 different observables (Pauli operators).
        3. Compile circuit and align observables with backend layout.
        4. Use Estimator primitive to compute expectation values.
        5. Extract and flatten results from the structured output.
        6. Plot as a bar chart with matplotlib.
"""
