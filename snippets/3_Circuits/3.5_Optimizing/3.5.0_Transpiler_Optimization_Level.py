# Flashcard: Setting transpiler optimization levels in Qiskit
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, random_unitary
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke

# --- Step 1: Create a 2-qubit random unitary circuit ---
UU = random_unitary(4, seed=12345)   # 4x4 random unitary matrix for 2 qubits
rand_U = UnitaryGate(UU)             # Wrap as a Qiskit gate

qc = QuantumCircuit(2)
qc.append(rand_U, [0, 1])            # Apply the random unitary
qc.swap(0, 1)                        # Apply a SWAP gate
print("Original circuit:\n", qc)

# --- Step 2: Define a helper function for 2-qubit fidelity ---
def trace_to_fidelity_2q(trace: float) -> float:
        # Converts a 2-qubit trace into a fidelity value
        return (4.0 + trace * trace.conjugate()) / 20.0

# --- Step 3: Select a mock backend ---
backend = FakeSherbrooke()

# --- Step 4: Transpile with different optimization levels ---
optimization_levels = [0, 1, 2, 3]

transpiled_circuits = {}
for level in optimization_levels:
        print(f"\n--- Transpiling at optimization level {level} ---")
        pass_manager = generate_preset_pass_manager(
                optimization_level=level,
                backend=backend,
                seed_transpiler=12345
        )
        transpiled_qc = pass_manager.run(qc)
        transpiled_circuits[level] = transpiled_qc
        print(transpiled_qc)  # Display transpiled circuit

# --- Step 5: Transpile at level 3 with approximation ---
pass_manager_approx = generate_preset_pass_manager(
        optimization_level=3,
        approximation_degree=0.99,  # Allows slight approximation in 2-qubit gate resynthesis
        backend=backend,
        seed_transpiler=12345,
)
qc_t3_approx = pass_manager_approx.run(qc)
print("\n--- Transpiled at level 3 with approximation ---")
print(qc_t3_approx)

# --- Step 6: Compare unitaries of exact vs approximate ---
# Reduce circuits to 2-qubit active system
qc_t3_exact_small = QuantumCircuit.from_instructions(transpiled_circuits[3])
qc_t3_approx_small = QuantumCircuit.from_instructions(qc_t3_approx)

# Compute fidelity with original random unitary
exact_fid = trace_to_fidelity_2q(
        np.trace(np.dot(Operator(qc_t3_exact_small).adjoint().data, UU))
)
approx_fid = trace_to_fidelity_2q(
        np.trace(np.dot(Operator(qc_t3_approx_small).adjoint().data, UU))
)
print(f"\nSynthesis fidelity\nExact: {exact_fid:.3f}\nApproximate: {approx_fid:.3f}")

"""
SUMMARY:
- Demonstrates transpiler optimization levels 0-3 and their effect.
- Steps executed:
        1. Create a 2-qubit circuit with a random unitary and a SWAP gate.
        2. Define a helper function to convert trace to 2-qubit fidelity.
        3. Choose a mock backend (FakeSherbrooke).
        4. Transpile the circuit at optimization levels 0,1,2,3 and print results.
        5. Transpile at level 3 with approximation_degree=0.99.
        6. Compute and print fidelity of level 3 exact and approximate circuits against original unitary.
- Key points:
  * Higher optimization levels reduce 2-qubit gate count and improve hardware efficiency.
  * Approximation can further reduce gates with minor fidelity loss.
  * Transpiler allows tuning trade-offs between compile time, gate count, and circuit fidelity.
"""
