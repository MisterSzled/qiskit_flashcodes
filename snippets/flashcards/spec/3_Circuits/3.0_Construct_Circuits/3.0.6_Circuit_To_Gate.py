from qiskit import QuantumCircuit

qc_a = QuantumCircuit(4)
qc_b = QuantumCircuit(2)
qc_b.y(0)
qc_b.z(1)

# Convert qc_b to Gate and add control
gate = qc_b.to_gate().control()

# Append controlled gate to qc_a
qc_a.append(gate, [0, 1, 3])
print("qc_a after appending qc_b as a controlled gate:")
print(qc_a)

"""
Summary:
- Demonstrates converting a circuit to a Gate and controlling it.
- Steps:
        1. Create qc_b.
        2. Convert qc_b to Gate.
        3. Add a control with `.control()`.
        4. Append controlled gate to qc_a.
"""
