# Flashcard 2.0.3: Plot estimator results with error bars
# Demonstrates:
# - Extracting standard errors from Estimator results
# - Adding error bars to matplotlib bar plots

import numpy as np
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.transpiler import generate_preset_pass_manager

# Step 1: Build quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.crx(1.5, 0, 1)

# Step 2: Define observables
observables_labels = ["ZZ", "XX", "YZ", "ZY", "XY", "XZ", "ZX"]
observables = [SparsePauliOp(label) for label in observables_labels]

# Step 3: Setup service and backend
service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True)

# Step 4: Compile circuit and apply layout
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)
isa_observables = [op.apply_layout(isa_circuit.layout) for op in observables]

# Step 5: Prepare observables for Estimator
reshaped_ops = np.fromiter(isa_observables, dtype=object).reshape((7, 1))

# Step 6: Run Estimator
estimator = Estimator(backend)
job = estimator.run([(isa_circuit, reshaped_ops)])
result = job.result()[0]
exp_val = result.data.evs
standard_error = result.data.stds
print("[RESULT]", result)

# Step 7: Plot results with error bars
_, ax = plt.subplots()
ax.bar(
        observables_labels,
        exp_val.flatten(),
        yerr=standard_error.flatten(),   # Error bars
        capsize=2                        # Small cap lines at error ends
)
ax.set_title("Expectation values (with standard errors)")
plt.show()

"""
SUMMARY:
- Demonstrates adding error bars to estimator visualization.
- Steps:
        1. Build circuit and observables as before.
        2. Run Estimator and extract expectation values + standard errors.
        3. Use matplotlib bar plot with `yerr` to add error bars.
        4. Add a title and show the figure.
"""
