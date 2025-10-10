from qiskit.circuit.library.n_local import n_local

two_local = n_local(3, rotation_blocks="rx", entanglement_blocks="cz")

# Assign all parameters to 0
bound_circuit = two_local.assign_parameters(
        {p: 0 for p in two_local.parameters}
)

print("Bound N-local circuit (all parameters = 0):")
print(bound_circuit.decompose())

"""
Summary:
- Demonstrates assigning parameters in N-local circuits.
- Steps:
        1. Create an N-local circuit.
        2. Assign all parameters to 0.
        3. Print the decomposed version of the bound circuit.
"""
