# Import an OpenQASM 2 program directly from a string
# Demonstrates qiskit.qasm2.loads()

import qiskit.qasm2

# Define a simple OpenQASM 2 program as a raw string
program = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];
measure q -> c;
"""

# Convert to a QuantumCircuit
circuit = qiskit.qasm2.loads(program)

print("Imported OpenQASM 2 circuit from string:")
print(circuit)

"""
SUMMARY:
- Demonstrates OpenQASM 2 import via qasm2.loads().
Steps:
        1. Write a QASM2 program as a multi-line string.
        2. Use qiskit.qasm2.loads() to parse and convert to a QuantumCircuit.
        3. Print the circuit to confirm import worked.
"""
