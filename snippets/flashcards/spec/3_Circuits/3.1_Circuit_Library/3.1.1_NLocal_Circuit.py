from qiskit.circuit.library.n_local import n_local

# Create an N-local circuit with:
# - 3 qubits
# - RX gates as rotation blocks
# - CZ gates as entangling blocks
two_local = n_local(3, rotation_blocks="rx", entanglement_blocks="cz")

print("N-local circuit structure:")
print(two_local)

# List circuit parameters
print("Parameters in the circuit:")
print(two_local.parameters)

"""
Summary:
- Demonstrates N-local circuits (used in variational algorithms).
- Steps:
        1. Import `n_local` from qiskit.circuit.library.n_local.
        2. Build a circuit with 3 qubits, RX for rotations, CZ for entanglement.
        3. Print the circuit and its parameters.
"""
