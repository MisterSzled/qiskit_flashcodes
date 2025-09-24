from qiskit import QuantumCircuit, transpile

# Build circuit with H and CX
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
print("Original circuit:\n", qc)

# Transpile without specifying backend (default optimizations only)
qc_trans = transpile(qc)
print("Transpiled circuit:\n", qc_trans)

"""
SUMMARY:
- transpile() rewrites a circuit into an equivalent form.
- Ensures compliance with backend requirements (basis gates, connectivity).
- Steps:
        1. Create circuit.
        2. Call transpile(circuit).
        3. Inspect rewritten version.
"""
