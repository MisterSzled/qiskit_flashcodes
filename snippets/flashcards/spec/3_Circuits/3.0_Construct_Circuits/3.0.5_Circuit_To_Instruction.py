from qiskit import QuantumCircuit

qc_a = QuantumCircuit(4)
qc_b = QuantumCircuit(2, name="qc_b")
qc_b.y(0)
qc_b.z(1)

# Convert qc_b into an Instruction and append to qc_a
inst = qc_b.to_instruction()
qc_a.append(inst, [1, 3])
print("qc_a after appending qc_b as an instruction:")
print(qc_a)

"""
Summary:
- Demonstrates converting a circuit into an instruction and appending it.
- Steps:
        1. Create qc_a and qc_b.
        2. Convert qc_b to instruction with `to_instruction`.
        3. Append it to qc_a on qubits [1,3].
"""
