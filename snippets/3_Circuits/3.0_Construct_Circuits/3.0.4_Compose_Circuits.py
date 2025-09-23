from qiskit import QuantumCircuit

qc_a = QuantumCircuit(4)
qc_a.x(0)  # Apply X gate to qubit 0

qc_b = QuantumCircuit(2, name="qc_b")
qc_b.y(0)
qc_b.z(1)

# Compose qc_b into qc_a on qubits [1,3]
combined = qc_a.compose(qc_b, qubits=[1, 3])
print("Composed circuit (qc_a with qc_b mapped to qubits [1,3]):")
print(combined)

"""
Summary:
- Demonstrates combining two circuits with `compose`.
- Steps:
        1. Create qc_a with 4 qubits.
        2. Create qc_b with 2 qubits.
        3. Map qc_b’s qubits (0→1, 1→3 of qc_a).
        4. Produce a new composed circuit.
"""
