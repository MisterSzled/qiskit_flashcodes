# 4.2.7 Simulating with Qiskit Aer
# Demonstrates running a quantum circuit on a simulator backend.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Step 1: Build a simple circuit
qc = QuantumCircuit(2, 2)
qc.h(0)            # Put qubit 0 into superposition
qc.cx(0, 1)        # Entangle qubits 0 and 1
qc.measure([0, 1], [0, 1])
print("Quantum circuit:\n", qc)

# Step 2: Choose an Aer simulator backend
sim = AerSimulator()

# Step 3: Run the simulation
job = sim.run(qc, shots=1000)  # Run 1000 repetitions
result = job.result()

# Step 4: Get counts of measurement results
counts = result.get_counts(qc)
print("Simulation counts:", counts)

# Optional: Visualize (requires matplotlib inline)
# plot_histogram(counts).show()

"""
SUMMARY:
- Demonstrates simulating a circuit using Qiskit Aer.
- Steps:
        1. Build a Bell-state circuit.
        2. Select AerSimulator backend.
        3. Run simulation with chosen number of shots.
        4. Collect and display measurement results.
"""
