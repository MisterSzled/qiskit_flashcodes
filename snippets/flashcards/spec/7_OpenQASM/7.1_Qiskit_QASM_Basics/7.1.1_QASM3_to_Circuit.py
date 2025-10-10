# 7.0.1 Convert OpenQASM3 to QuantumCircuit
# Demonstrates importing an OpenQASM 3 program into Qiskit.

import qiskit.qasm3

program = """
OPENQASM 3.0;
include "stdgates.inc";

qubit[2] q;
h q[0];
cx q[0], q[1];
"""

# Convert QASM3 string to QuantumCircuit
circuit = qiskit.qasm3.loads(program)

print("Converted circuit:\n")
print(circuit)

"""
SUMMARY:
- Demonstrates conversion of OpenQASM 3 string → QuantumCircuit.
Steps:
        1. Define OpenQASM3 program as string.
        2. Use qiskit.qasm3.loads() to import.
        3. Inspect converted circuit object.
"""
