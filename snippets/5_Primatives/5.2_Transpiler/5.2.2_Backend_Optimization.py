# 5.2.2 Transpile with Backend and Optimization
# Demonstrates backend-aware transpilation with optimization levels.

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Circuit with operations not native to all backends
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
print("Original circuit:\n", qc)

# Choose Aer simulator as target backend
backend = AerSimulator()

# Transpile with backend constraints and optimization level
qc_trans = transpile(qc, backend=backend, optimization_level=3)
print("Backend-aware transpiled circuit:\n", qc_trans)

"""
SUMMARY:
- transpile(circuit, backend, optimization_level) adapts to real hardware.
- optimization_level ∈ {0,1,2,3}:
        0 = no optimization,
        3 = max optimization (fewest gates/depth).
- Backend determines allowed basis gates + qubit connectivity.
"""
