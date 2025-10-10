# Export a QuantumCircuit to OpenQASM 2
# Demonstrates qasm2.dumps() and qasm2.dump()

from qiskit import QuantumCircuit, qasm2

# Build a small example circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Export to string
program_str = qasm2.dumps(qc)
print("Exported circuit as QASM2 string:\n", program_str)

# Export to file
qasm2.dump(qc, "exported_qasm2.qasm")
print("Exported circuit to file: exported_qasm2.qasm")

"""
SUMMARY:
- Demonstrates OpenQASM 2 export.
Steps:
        1. Create a QuantumCircuit with H + CX + measurement.
        2. Export to a QASM2 string with dumps().
        3. Export to a QASM2 file with dump().
"""
