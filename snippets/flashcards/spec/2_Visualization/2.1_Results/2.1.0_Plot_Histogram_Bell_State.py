# Flashcard 2.0.0: Plot histogram of Bell state measurement results (Aer version)
# Demonstrates how to:
# 1. Build a simple Bell state circuit
# 2. Run the circuit with Aer Sampler primitive
# 3. Visualize measurement results using plot_histogram
# 4. Show the figure explicitly in a non-notebook environment

from qiskit.circuit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer.primitives import SamplerV2  # Aer Sampler (local simulator)

# Step 1: Create a 2-qubit Bell state circuit
bell = QuantumCircuit(2)
bell.h(0)        # Put qubit 0 in superposition
bell.cx(0, 1)    # Entangle qubit 0 with qubit 1
bell.measure_all()
print("[INFO] Bell state circuit created.")

# Step 2: Initialize the Aer Sampler
sampler = SamplerV2()

# Step 3: Run the circuit with the Sampler
print("[INFO] Running Bell state job on local simulator...")
job = sampler.run([bell])
result = job.result()
print("[RESULT]", result)

# Step 4: Visualize the measurement results
print("[INFO] Plotting histogram...")
fig = plot_histogram(result[0].data.meas.get_counts())

# Step 5: Show or save the figure
fig.show()          # Opens interactive window (if supported)
fig.savefig("bell_histogram.png")  # Save instead of showing


"""
SUMMARY:
- This flashcard demonstrates how to visualize results with `plot_histogram` using Aer.
- Steps:
        1. Build a Bell state quantum circuit with H and CX gates.
        2. Initialize Aer Sampler (local simulator).
        3. Run the circuit and collect results.
        4. Use `plot_histogram` to generate a matplotlib figure.
        5. Show or save the histogram explicitly in script environments.
"""
