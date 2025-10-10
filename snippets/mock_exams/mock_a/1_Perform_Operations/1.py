"""
1. Which one of the following code fragments will generate the given output?

[[ 0.+0.j  0.+0.j  1.+0.j  0.+0.j]
[ 0.+0.j  0.+0.j  0.+0.j  1.+0.j]
[ 1.+0.j  0.+0.j  0.+0.j  0.+0.j]
[ 0.+0.j  1.+0.j  0.+0.j  0.+0.j]]

a. p = Pauli('XI'); print(p.to_matrix())
b. p = Pauli('IX'); print(p.to_matrix())
c. p = Pauli('-XI'); print(p.to_matrix())
d. p = Pauli('XZ'); print(p.to_matrix())
"""

from qiskit.quantum_info.operators import Pauli

# Test each choice by constructing Pauli operators
# and printing their matrix representations

print("Option a: Pauli('XI') →\n", Pauli('XI').to_matrix(), "\n")
print("Option b: Pauli('IX') →\n", Pauli('IX').to_matrix(), "\n")
print("Option c: Pauli('-XI') →\n", Pauli('-XI').to_matrix(), "\n")
print("Option d: Pauli('XZ') →\n", Pauli('XZ').to_matrix(), "\n")
