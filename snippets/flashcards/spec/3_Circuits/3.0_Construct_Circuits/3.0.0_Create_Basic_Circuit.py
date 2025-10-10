from qiskit import QuantumCircuit

print("Creating a quantum circuit with 2 qubits...")
qc = QuantumCircuit(2)  # Create a circuit with 2 qubits

# Access the circuit's qubits attribute
print("Qubit register objects in the circuit:")
print(qc.qubits)  # Shows Qubit objects and their indices


print(qc)
"""
Summary:
- Demonstrates creating a basic QuantumCircuit with 2 qubits.
- Accessed the `qubits` attribute to inspect the qubits inside the circuit.
- Steps:
        1. Import QuantumCircuit.
        2. Create a circuit with 2 qubits.
        3. Print out the qubits to show their representation.
"""
