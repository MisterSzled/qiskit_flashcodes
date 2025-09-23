from qiskit.circuit.library import NLocal

# Create an N-local circuit with:
# - 3 qubits
# - RX gates as rotation blocks
# - CZ gates as entangling blocks
two_local = NLocal(3, "rx", "cz")

print("N-local circuit structure:")
print(two_local)

# List circuit parameters
print("Parameters in the circuit:")
print(two_local.parameters)

"""
Summary:
- Demonstrates N-local circuits (used in variational algorithms).
- Steps:
        1. Import NLocal.
        2. Build a circuit with 3 qubits, RX for rotations, CZ for entanglement.
        3. Print the circuit and its parameters.
"""
