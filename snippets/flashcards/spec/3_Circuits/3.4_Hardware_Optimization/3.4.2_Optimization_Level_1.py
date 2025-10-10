# Flashcard: Transpilation at optimization level 1 (light optimization)
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import random_unitary
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke

# --- Step 1: Create a 2-qubit random unitary circuit ---
UU = random_unitary(4, seed=123)
qc = QuantumCircuit(2)
qc.append(UnitaryGate(UU), [0, 1])
qc.swap(0, 1)
print("Original circuit:\n", qc)

# --- Step 2: Select backend and transpile ---
backend = FakeSherbrooke()
pass_manager = generate_preset_pass_manager(
        optimization_level=1,  # Level 1: light optimization
        backend=backend,
        seed_transpiler=123
)
qc_t1 = pass_manager.run(qc)
print("\nTranspiled circuit at optimization level 1:\n", qc_t1)

"""
SUMMARY:
- Demonstrates optimization level 1: light optimization.
- Steps executed:
        1. Create a 2-qubit circuit with random unitary and SWAP.
        2. Generate a preset pass manager with optimization_level=1.
        3. Run pass manager to transpile the circuit.
        4. Print transpiled circuit.
- Key points:
  * Optimizes 1-qubit gates, performs inverse cancellations.
  * Layout uses TrivialLayout first, then minimal SWAP search if needed.
  * Circuit may reduce gate count without deep optimization.
"""
