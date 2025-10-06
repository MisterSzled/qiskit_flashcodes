# 16. Which error mitigation technique can be applied using resilience options?
# a. Pauli twirling
# b. Dynamical decoupling
# c. Zero Noise Extrapolation
# d. Full quantum error correction
#
# This example demonstrates Zero Noise Extrapolation (ZNE) conceptually on Aer.

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

# --- Step 1: Create a simple circuit ---
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

# --- Step 2: Define "noise scaling" levels ---
# We'll simulate noise by repeating H gates to amplify noise
scale_factors = [1, 2, 3]  # Conceptual: more H repetitions -> more noise

# --- Step 3: Run circuit with scaled noise ---
simulator = AerSimulator(noise_model=None)  # No real noise; we conceptually demonstrate ZNE
measured_means = []

for scale in scale_factors:
        qc_scaled = QuantumCircuit(1)
        for _ in range(scale):
                qc_scaled.h(0)  # Repeated gate to simulate scaled "noise"
        qc_scaled.measure_all()

        # Run simulation
        result = simulator.run(qc_scaled, shots=1000).result()
        counts = result.get_counts()
        prob_1 = counts.get('1', 0) / 1000
        measured_means.append(prob_1)

print("Measured probabilities at different noise scales:", measured_means)

# --- Step 4: Conceptual ZNE extrapolation ---
# We can fit a line through the scaled probabilities and extrapolate back to "zero noise"
coeffs = np.polyfit(scale_factors, measured_means, 1)
extrapolated_zero_noise = np.polyval(coeffs, 0)
print("Extrapolated zero-noise probability (conceptual ZNE):", extrapolated_zero_noise)

"""
SUMMARY:
- Demonstrates the concept of Zero Noise Extrapolation (ZNE) locally.
- Steps:
        1. Build a simple circuit (H gate on |0>).
        2. "Scale noise" by repeating gates.
        3. Measure outcome probabilities for each scale.
        4. Extrapolate results back to zero noise.
- Key point:
    * ZNE is a resilience technique that reduces error impact.
    * In practice, Qiskit applies it automatically on IBM Runtime backends with resilience options.
"""
