# Demonstrates what transpilation is:
#   - Rewriting a circuit to match hardware constraints (basis gates, connectivity)
#   - Optimizing depth to reduce noise

from qiskit import QuantumCircuit, transpile

# Step 1: Build a small circuit with gates not natively supported on real devices
qc = QuantumCircuit(2)
qc.h(0)        # Hadamard on qubit 0
qc.cx(0, 1)    # CNOT from qubit 0 to qubit 1
qc.cx(1, 0)    # CNOT from qubit 1 to qubit 0
print("Original circuit:\n", qc)

# Step 2: Transpile for a fake backend (basis gates vary by hardware)
# For this demo, no backend given = use default basis gates
transpiled = transpile(qc, optimization_level=1)
print("\nTranspiled circuit:\n", transpiled)

"""
SUMMARY:
- Shows the basic purpose of transpilation.
- Steps executed:
        1. Create a 2-qubit circuit (H + 2 CNOTs).
        2. Call transpile() to rewrite it in terms of allowed basis gates.
        3. Print original vs transpiled circuit.
"""
