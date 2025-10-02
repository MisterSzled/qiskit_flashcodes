from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate

qc = QuantumCircuit(1)

# Append an HGate to qubit 0
qc.append(HGate(), [0])
print("Circuit data after appending HGate:")
print(qc.data)

"""
Summary:
- Demonstrates the `append` method for adding instructions.
- Steps:
        1. Import HGate.
        2. Create 1-qubit circuit.
        3. Append an HGate to qubit 0.
        4. Print the circuit data to confirm.
"""
