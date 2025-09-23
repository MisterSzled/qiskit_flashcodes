# Flashcard 2.0.1: Customize histogram options
# Demonstrates:
# - Running the same circuit multiple times with different shot counts
# - Customizing histogram appearance (legend, sorting, colors, labels, figsize)

from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.circuit import QuantumCircuit
from qiskit.visualization import plot_histogram

# Setup service and backend
print("[INFO] Connecting to service...")
service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True)

# Bell state circuit
bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(bell)

# Create sampler
sampler = Sampler(backend)

# First execution (default shots = 4096)
job1 = sampler.run([isa_circuit])
result1 = job1.result()
print("[INFO] First run complete.")

# Second execution with fewer shots
sampler.options.default_shots = 1000
job2 = sampler.run([isa_circuit])
result2 = job2.result()
print("[INFO] Second run complete.")

# Plot combined histogram with options
print("[INFO] Plotting histogram with custom options...")
fig = plot_histogram(
        [
                result1[0].data.meas.get_counts(),
                result2[0].data.meas.get_counts(),
        ],
        legend=["first", "second"],   # Labels for each run
        sort="desc",                   # Sort bars descending
        figsize=(15, 12),              # Figure size in inches
        color=["orange", "black"],     # Bar colors
        bar_labels=False               # Disable labels above bars
)
fig.show()

"""
SUMMARY:
- Demonstrates customization of histogram visualization.
- Steps:
        1. Build a Bell state circuit and compile it for backend.
        2. Run circuit twice (4096 shots, then 1000 shots).
        3. Collect results and combine them.
        4. Customize histogram with legend, sorting, figure size, colors, and labels.
        5. Show final combined histogram.
"""
