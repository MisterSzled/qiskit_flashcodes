# Import an OpenQASM 3 program from a string
# Demonstrates qiskit.qasm3.loads()

import qiskit.qasm3

program = """
OPENQASM 3.0;
include "stdgates.inc";

qubit[2] q;
bit[2] c;

h q[0];
cx q[0], q[1];
c = measure q;
"""

circuit = qiskit.qasm3.loads(program)
print("Imported OpenQASM 3 circuit from string:")
print(circuit)

"""
SUMMARY:
- Demonstrates importing OpenQASM 3 programs.
Steps:
        1. Define QASM3 program with qubits, gates, measurements.
        2. Use qiskit.qasm3.loads() to convert into QuantumCircuit.
        3. Print to confirm import succeeded.
"""
