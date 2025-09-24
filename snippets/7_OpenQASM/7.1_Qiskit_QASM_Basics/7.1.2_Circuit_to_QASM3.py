# 7.0.2 Export QuantumCircuit to OpenQASM3
# Demonstrates exporting a QuantumCircuit into OpenQASM 3 format.

from qiskit import QuantumCircuit
from qiskit.qasm3 import dumps

# Build a simple Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Export as OpenQASM 3 string
qasm_string = dumps(qc)

print("Exported OpenQASM 3:\n")
print(qasm_string)

"""
SUMMARY:
- Shows exporting from QuantumCircuit to OpenQASM 3.
Steps:
        1. Build circuit in Qiskit.
        2. Use qiskit.qasm3.dumps() to export as text.
        3. Print OpenQASM 3 code.
"""
