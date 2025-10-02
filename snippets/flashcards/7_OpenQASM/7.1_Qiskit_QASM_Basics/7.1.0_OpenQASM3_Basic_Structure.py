# 7.0.0 OpenQASM3 Basic Structure
# Demonstrates the structure of an OpenQASM 3 program (header, includes, registers, gates).

program = """
OPENQASM 3.0;
include "stdgates.inc";

const n = 3;          // define number of qubits
qubit[n] q;           // quantum register
bit[n] c;             // classical register

h q[0];               // apply Hadamard
for k in [0:n-1] {    // loop for entanglement
        cnot q[k], q[k+1];
}

c = measure q;        // measure all qubits
"""

print("OpenQASM 3 program:\n")
print(program)

"""
SUMMARY:
- Shows basic structure of OpenQASM 3:
        1. Header (`OPENQASM 3.0;`).
        2. Include standard gates.
        3. Define constants, qubit + bit registers.
        4. Apply gates, use loop, measure.
- Demonstrates imperative style and clear block structure.
"""
