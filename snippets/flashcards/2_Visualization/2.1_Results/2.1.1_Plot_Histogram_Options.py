# Flashcard 2.1.1: Customize histogram options (Aer version)
# Demonstrates:
# - Running the same circuit multiple times with different shot counts
# - Customizing histogram appearance (legend, sorting, colors, labels, figsize)

from qiskit.circuit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer.primitives import SamplerV2  # Aer Sampler (local simulator)

# Step 1: Build a Bell state circuit
bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()
print("[INFO] Bell state circuit created.")

# Step 2: Create Aer Sampler
sampler = SamplerV2()

# Step 3: First execution (default shots = 4096)
job1 = sampler.run([bell], shots=4096)
result1 = job1.result()
print("[INFO] First run complete with 4096 shots.")

# Step 4: Second execution with fewer shots (1000)
job2 = sampler.run([bell], shots=1000)
result2 = job2.result()
print("[INFO] Second run complete with 1000 shots.")

# Step 5: Plot combined histogram with custom options
print("[INFO] Plotting histogram with custom options...")
fig = plot_histogram(
        [
                result1[0].data.meas.get_counts(),
                result2[0].data.meas.get_counts(),
        ],
        legend=["first (4096 shots)", "second (1000 shots)"],  # Labels for each run
        sort="desc",                  # Sort bars descending
        figsize=(15, 12),             # Figure size in inches
        color=["orange", "black"],    # Bar colors
        bar_labels=False              # Disable labels above bars
)

# Step 6: Save or show figure
fig.savefig("bell_histogram.png")
print("[INFO] Histogram saved as bell_histogram.png")
# fig.show()  # Uncomment to open interactive window if supported

print("4096-shot counts:", result1[0].data.meas.get_counts())
print("1000-shot counts:", result2[0].data.meas.get_counts())

"""
SUMMARY:
- Demonstrates customization of histogram visualization with Aer simulator.
- Steps:
        1. Build a Bell state circuit.
        2. Run twice with different shot counts (4096, 1000).
        3. Collect results and combine them.
        4. Customize histogram: legend, sorting, figsize, colors, labels.
        5. Save (or show) the final histogram.
"""
