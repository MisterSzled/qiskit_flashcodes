from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
print("Initial circuit data:", qc.data)  # Should be empty

# Add an X gate on qubit 0
qc.x(0)
print("Circuit data after adding X gate:")
print(qc.data)  # List of CircuitInstruction objects

"""
Summary:
- Shows how adding gates modifies a circuit’s `data` attribute.
- Steps:
        1. Create 2-qubit circuit.
        2. Check empty data list.
        3. Apply X gate to qubit 0.
        4. Print circuit instructions list.
"""
