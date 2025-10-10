# Flashcard 2.2.0: Create a Statevector from a quantum circuit
# Demonstrates:
# - Building a quantum circuit
# - Creating a Statevector object from the circuit
# - Printing the raw vector representation

from math import pi
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Step 1: Build a 2-qubit Bell-like state
qc = QuantumCircuit(2)
qc.h(0)                # Put qubit 0 in superposition
qc.crx(pi / 2, 0, 1)   # Controlled rotation around X-axis
print("[INFO] Quantum circuit created.")

# Step 2: Convert the circuit into a Statevector object
psi = Statevector(qc)
print("[INFO] Statevector object created.")

# Step 3: Show the statevector amplitudes
print("[RESULT] Statevector amplitudes:\n", psi)

"""
SUMMARY:
- Demonstrates how to create a Statevector from a quantum circuit.
- Steps:
        1. Build a quantum circuit (Hadamard + controlled rotation).
        2. Use `Statevector(circuit)` to simulate the final quantum state.
        3. Print the amplitudes of the quantum state.
"""
