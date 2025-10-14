# 9. Given the code fragment below, which one of the following images could be produced?
#
# from qiskit import QuantumCircuit
# from qiskit import generate_preset_pass_manager
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0,1)
# pass_manager = generate_preset_pass_manager(
#     optimization_level=3,
#     coupling_map=[[0, 1], [1, 2]],
#     basis_gates=['h', 'swap', 'cx'],
#     initial_layout=[0, 2]
# )
# tqc = pass_manager.run(qc)
# tqc.draw(output="mpl")
#
# a. A simple H followed by a CX (unchanged circuit)
# b. A circuit with additional SWAP gates inserted due to layout constraints
# c. A single SWAP gate only (no H or CX)
# d. An empty circuit (no operations)

from qiskit import QuantumCircuit
from qiskit import generate_preset_pass_manager
from qiskit.visualization import circuit_drawer

# --- Step 1: Create the original logical circuit ---
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

print("\nOriginal circuit:")
print(qc.draw())

# --- Step 2: Define the preset pass manager ---
pass_manager = generate_preset_pass_manager(
        optimization_level=3,
        coupling_map=[[0, 1], [1, 2]],  # physical connectivity
        basis_gates=['h', 'swap', 'cx'],
        initial_layout=[0, 2]           # map logical qubits [0, 1] → physical qubits [0, 2]
)

# --- Step 3: Transpile (optimize + map) the circuit ---
tqc = pass_manager.run(qc)

print("\nTranspiled circuit:")
print(tqc.draw())

# --- Step 4: Save visualizations for comparison ---
circuit_drawer(qc, output="mpl", filename="q9_original_circuit.png")
circuit_drawer(tqc, output="mpl", filename="q9_transpiled_circuit.png")

print("\nSaved 'q9_original_circuit.png' and 'q9_transpiled_circuit.png'")

"""
SUMMARY:
        - This snippet demonstrates how Qiskit's pass manager (with optimization_level=3)
                modifies a circuit according to coupling_map and basis_gates constraints.
        - initial_layout remaps logical qubits → physical qubits, potentially introducing SWAPs.
        - The transpiled circuit ('tqc') is drawn and saved for visual inspection.
        - One of the answer choices matches the resulting layout with extra SWAP(s).
"""
