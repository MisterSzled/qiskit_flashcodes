from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)  # Add X gate to qubit 0

# Each instruction has a definition (a decomposition into primitive gates).
definition_circuit = qc.data[0].operation.definition
print("Definition circuit for the X gate:")
print(definition_circuit)

print(qc)
"""
Summary:
- Demonstrates retrieving the definition of an instruction.
- Steps:
        1. Create circuit with 1 qubit.
        2. Apply an X gate.
        3. Access the definition of the X gate (as a circuit).
        4. Print the definition circuit.
"""
