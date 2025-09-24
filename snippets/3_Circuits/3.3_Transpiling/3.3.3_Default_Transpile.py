# Demonstrates using the simple transpile() function with optimization levels
# Optimization levels: 0 (none), 1 (light), 2 (medium), 3 (heavy)

from qiskit import QuantumCircuit, transpile

# Step 1: Build a sample circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 0)
print("Original circuit:\n", qc)

# Step 2: Transpile with increasing optimization levels
for level in range(4):
        print(f"\nTranspiling with optimization_level={level}")
        new_circ = transpile(qc, optimization_level=level)
        print(new_circ)

"""
SUMMARY:
- Shows quick transpile() function with optimization_level flag.
- Steps executed:
        1. Create 2-qubit circuit (H + CNOTs).
        2. Transpile with levels 0-3.
        3. Print differences in optimized results.
"""
