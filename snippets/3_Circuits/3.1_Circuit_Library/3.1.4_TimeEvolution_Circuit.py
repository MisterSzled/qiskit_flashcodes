from qiskit.circuit.library import PauliEvolutionGate
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

# Initial state with Hadamard on qubit 1
state = QuantumCircuit(3)
state.h(1)

# Define Hamiltonian for time evolution
hamiltonian = SparsePauliOp(["ZZI", "IZZ"])

# Create evolution gate with time = 1
evolution = PauliEvolutionGate(hamiltonian, time=1)

# Append evolution gate to state
state.compose(evolution, inplace=True)

print("State after time evolution under Hamiltonian:")
print(state)

"""
Summary:
- Demonstrates time evolution circuits with PauliEvolutionGate.
- Steps:
        1. Prepare initial state (H on qubit 1).
        2. Define Hamiltonian using SparsePauliOp.
        3. Build PauliEvolutionGate with time=1.
        4. Compose evolution into circuit.
        5. Print resulting circuit.
"""
