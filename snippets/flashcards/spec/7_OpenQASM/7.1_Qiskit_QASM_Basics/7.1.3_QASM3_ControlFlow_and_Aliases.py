# 7.0.3 OpenQASM3 Control Flow & Aliases
# Demonstrates advanced OpenQASM 3 features:
#   - Aliasing qubits
#   - Custom gates
#   - Control flow (while/if)

import qiskit.qasm3

program = """
OPENQASM 3.0;
include "stdgates.inc";

input float[64] a;
qubit[3] q;
bit[2] mid;
bit[3] out;

let aliased = q[0:1];   // alias sub-register

gate my_gate(a) c, t {
        gphase(a / 2);
        ry(a) c;
        cx c, t;
}

my_gate(a) aliased[0], q[1];
mid[0] = measure q[0];
mid[1] = measure q[1];

while (mid == "00") {   // classical feedback
        reset q[0];
        reset q[1];
        my_gate(a) q[0], q[1];
}
out = measure q;
"""

# Import into QuantumCircuit
circuit = qiskit.qasm3.loads(program)

print("Imported circuit with control flow:\n")
print(circuit)

"""
SUMMARY:
- Demonstrates advanced OpenQASM 3 structures:
        1. Aliasing registers.
        2. Defining custom gates.
        3. While loop with classical condition.
        4. Reset + feedback.
- Imported into Qiskit for execution/analysis.
"""
