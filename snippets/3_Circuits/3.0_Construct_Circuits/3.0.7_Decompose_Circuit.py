from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Convert to instruction, then append back
inst = qc.to_instruction()
big_qc = QuantumCircuit(2)
big_qc.append(inst, [0, 1])

# Decompose to see underlying structure
decomposed = big_qc.decompose()
print("Decomposed circuit:")
print(decomposed)

"""
Summary:
- Shows how to decompose an instruction into its primitive gates.
- Steps:
        1. Build qc with H and CX gates.
        2. Convert qc to instruction, append to new circuit.
        3. Use `decompose()` to expand instruction into underlying gates.
"""
