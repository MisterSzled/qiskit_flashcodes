# Use custom instructions with OpenQASM 2 importer
# Demonstrates qasm2.CustomInstruction and qasm2.CustomClassical

import math
from qiskit import qasm2
from qiskit.circuit import Gate
from qiskit.circuit.library import RZXGate

# Define a custom 1-qubit gate with 2 parameters
class MyGate(Gate):
        def __init__(self, theta, phi):
                super().__init__("my", 1, [theta, phi])

# Define custom instruction mappings
custom_instructions = [
        qasm2.CustomInstruction("my", 2, 1, MyGate),
        qasm2.CustomInstruction("rzx", 1, 2, RZXGate),
]

# Define a QASM2 program using "my" and "rzx"
program = """
OPENQASM 2.0;
qreg q[2];
my(0.25, 0.125) q[0];
rzx(pi) q[0], q[1];
"""

circuit = qasm2.loads(program, custom_instructions=custom_instructions)
print("Imported circuit with custom instructions:")
print(circuit)

# Custom classical function
def add_one(x): return x + 1
custom_classical = [qasm2.CustomClassical("add_one", 1, add_one)]

program2 = """
OPENQASM 2.0;
qreg q[1];
rx(add_one(0.2)) q[0];
"""

circuit2 = qasm2.loads(program2, custom_classical=custom_classical)
print("Imported circuit with custom classical function:")
print(circuit2)

"""
SUMMARY:
- Demonstrates adding custom quantum gates and classical functions.
Steps:
        1. Define Python classes/functions for custom ops.
        2. Register them with CustomInstruction or CustomClassical.
        3. Import QASM2 programs that reference those names.
        4. Verify they are mapped to Qiskit gates/functions.
"""
