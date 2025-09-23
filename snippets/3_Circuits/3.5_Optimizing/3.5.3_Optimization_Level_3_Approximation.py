# Flashcard: Transpilation at optimization level 3 with approximation
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, random_unitary
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke

# --- Step 1: Create a 2-qubit random unitary circuit ---
UU = random_unitary(4, seed=2025)
qc = QuantumCircuit(2)
qc.append(UnitaryGate(UU), [0, 1])
qc.swap(0, 1)
print("Original circuit:\n", qc)

# --- Step 2: Select backend and transpile with high optimization and approximation ---
backend = FakeSherbrooke()
pass_manager = generate_preset_pass_manager(
        optimization_level=3,          # Level 3: high optimization
        approximation_degree=0.99,     # Allow slight approximation
        backend=backend,
        seed_transpiler=2025
)
qc_t3_approx = pass_manager.run(qc)
print("\nTranspiled circuit at optimization level 3 with approximation:\n", qc_t3_approx)

# --- Step 3: Compare fidelity to exact unitary ---
qc_t3_exact_small = QuantumCircuit.from_instructions(qc_t3_approx)
fidelity = lambda trace: (4 + trace * trace.conjugate()) / 20
exact_fid = fidelity(np.trace(np.dot(Operator(qc_t3_exact_small).adjoint().data, UU)))
print(f"\nApproximate circuit fidelity with original unitary: {exact_fid:.3f}")

"""
SUMMARY:
- Demonstrates optimization level 3: high optimization with approximation.
- Steps executed:
        1. Create a 2-qubit circuit with random unitary and SWAP.
        2. Transpile with optimization_level=3 and approximation_degree=0.99.
        3. Print transpiled approximate circuit.
        4. Compute fidelity between transpiled approximate circuit and original unitary.
- Key points:
  * Level 3 re-synthesizes 2-qubit blocks and reduces gate count aggressively.
  * Approximation allows fewer gates at small fidelity loss.
  * Useful for reducing circuit errors on noisy hardware.
"""
