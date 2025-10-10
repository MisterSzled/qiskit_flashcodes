# Compare QASM 2 vs QASM 3 import/export
# Demonstrates interoperability between versions

from qiskit import QuantumCircuit, qasm2
import qiskit.qasm3 as qasm3

# Build a reference circuit in Qiskit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Export to QASM2 and re-import
qasm2_str = qasm2.dumps(qc)
qc_from_qasm2 = qasm2.loads(qasm2_str)
print("Circuit round-tripped via QASM2:")
print(qc_from_qasm2)

# Export to QASM3 and re-import
qasm3_str = qasm3.dumps(qc)
qc_from_qasm3 = qasm3.loads(qasm3_str)
print("Circuit round-tripped via QASM3:")
print(qc_from_qasm3)

"""
SUMMARY:
- Demonstrates interoperability of QASM2 and QASM3.
Steps:
        1. Build a circuit in Qiskit.
        2. Export/import through QASM2 pipeline.
        3. Export/import through QASM3 pipeline.
        4. Compare circuits after round-trip.
"""
