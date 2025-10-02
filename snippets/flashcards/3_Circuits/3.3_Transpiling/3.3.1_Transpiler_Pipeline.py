# Demonstrates the six stages of the transpiler pipeline
# Stages: init, layout, routing, translation, optimization, scheduling

from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit import QuantumCircuit

# Step 1: Build a circuit needing transpilation
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 2)  # May not be directly supported on some backends
print("Original circuit:\n", qc)

# Step 2: Generate a preset staged pass manager (optimization level 1)
pm = generate_preset_pass_manager(optimization_level=1)
print("\nPassManager pipeline created with staged passes.")

# Step 3: Run the pass manager on our circuit
new_circ = pm.run(qc)
print("\nCircuit after staged passes:\n", new_circ)

"""
SUMMARY:
- Shows staged transpiler pipeline.
- Steps executed:
        1. Build a 3-qubit circuit.
        2. Generate a staged pass manager (includes all 6 stages).
        3. Run pass manager → transpiled circuit returned.
"""
