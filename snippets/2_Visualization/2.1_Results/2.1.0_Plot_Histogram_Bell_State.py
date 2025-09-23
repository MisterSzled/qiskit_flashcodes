# Flashcard 2.0.0: Plot histogram of Bell state measurement results
# Demonstrates how to:
# 1. Build a simple Bell state circuit
# 2. Run the circuit with the Sampler primitive
# 3. Visualize measurement results using plot_histogram
# 4. Show the figure explicitly in a non-notebook environment

from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.circuit import QuantumCircuit
from qiskit.visualization import plot_histogram

# Step 1: Connect to Qiskit Runtime Service
print("[INFO] Connecting to Qiskit Runtime Service...")
service = QiskitRuntimeService()

# Step 2: Choose an available backend (a real quantum device, not a simulator)
print("[INFO] Fetching least busy backend...")
backend = service.least_busy(simulator=False, operational=True)

# Step 3: Create a 2-qubit Bell state circuit
bell = QuantumCircuit(2)
bell.h(0)        # Put qubit 0 in superposition
bell.cx(0, 1)    # Entangle qubit 0 with qubit 1
bell.measure_all()
print("[INFO] Bell state circuit created.")

# Step 4: Optimize for backend
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(bell)

# Step 5: Run the circuit with the Sampler primitive
sampler = Sampler(backend)
print("[INFO] Submitting Bell state job...")
job = sampler.run([isa_circuit])
result = job.result()
print("[RESULT]", result)

# Step 6: Visualize the measurement results
print("[INFO] Plotting histogram...")
fig = plot_histogram(result[0].data.meas.get_counts())

# For scripts: explicitly show or save the figure
fig.show()          # Opens interactive window (if supported)
# fig.savefig("bell_histogram.png")  # Save instead of showing

"""
SUMMARY:
- This flashcard demonstrates how to visualize results with `plot_histogram`.
- Steps:
        1. Connect to IBM Quantum service and get a backend.
        2. Build a Bell state quantum circuit with H and CX gates.
        3. Optimize with a preset pass manager for the backend.
        4. Run using the `Sampler` primitive and collect results.
        5. Use `plot_histogram` to generate a matplotlib figure.
        6. Show or save the histogram explicitly in script environments.
"""
