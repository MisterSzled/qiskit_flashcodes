# Parse OpenQASM 2 in strict mode
# Demonstrates the "strict=True" option in qasm2.loads()

import qiskit.qasm2

# Program missing OPENQASM version line (normally tolerated)
program = """
include "qelib1.inc";
qreg q[1];
h q[0];
"""

# Relaxed mode (default) works
circuit = qiskit.qasm2.loads(program)
print("Relaxed mode accepted program:", circuit)

# Strict mode should reject it
try:
        qiskit.qasm2.loads(program, strict=True)
except Exception as e:
        print("Strict mode error:", e)

"""
SUMMARY:
- Demonstrates strict parsing in OpenQASM 2.
Steps:
        1. Write a QASM2 program missing the version line.
        2. Parse normally (accepted).
        3. Parse with strict=True (raises error).
"""
