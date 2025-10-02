# Import an OpenQASM 2 program from a file
# Demonstrates qiskit.qasm2.load()

import qiskit.qasm2

# Assume "myfile.qasm" exists on disk
circuit = qiskit.qasm2.load("myfile.qasm")

print("Imported OpenQASM 2 circuit from file:")
print(circuit)

"""
SUMMARY:
- Demonstrates OpenQASM 2 import via qasm2.load().
Steps:
        1. Prc the resulting QuantumCircuit.
"""
