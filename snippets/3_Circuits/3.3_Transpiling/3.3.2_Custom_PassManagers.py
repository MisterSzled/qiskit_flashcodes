# Demonstrates customizing PassManagers
# PassManager = collection of passes
# StagedPassManager = orchestrates multiple PassManagers

from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Optimize1qGates, RemoveBarriers
from qiskit import QuantumCircuit

# Step 1: Create a circuit with redundant gates
qc = QuantumCircuit(1)
qc.h(0)
qc.h(0)  # consecutive H gates cancel
qc.barrier()
print("Original circuit:\n", qc)

# Step 2: Build custom PassManager with chosen passes
pm = PassManager([Optimize1qGates(), RemoveBarriers()])
print("\nCustom PassManager created with optimization passes.")

# Step 3: Run pass manager on circuit
optimized = pm.run(qc)
print("\nOptimized circuit:\n", optimized)

"""
SUMMARY:
- Demonstrates customizing a transpilation workflow.
- Steps executed:
        1. Create redundant circuit (H,H + barrier).
        2. Build PassManager with Optimize1qGates + RemoveBarriers.
        3. Run → redundant gates/barrier removed.
"""
