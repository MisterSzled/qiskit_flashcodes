# Export a QuantumCircuit to OpenQASM 3
# Demonstrates qiskit.qasm3.dumps() and qiskit.qasm3.dump()

from qiskit import QuantumCircuit
from qiskit.qasm3 import dumps, dump

# Build example circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Export to string
program_str = dumps(qc)
print("Exported circuit as QASM3 string:\n", program_str)

# Export to file
with open("exported_qasm3.qasm", "w") as f:
        dump(qc, f)
print("Exported circuit to file: exported_qasm3.qasm")

"""
SUMMARY:
- Demonstrates exporting circuits to OpenQASM 3.
Steps:
        1. Build a small circuit with H, CX, measurement.
        2. Export as a string with dumps().
        3. Export to a file with dump().
"""
