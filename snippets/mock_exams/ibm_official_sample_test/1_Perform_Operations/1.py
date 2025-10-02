"""
Qiskit v2.x Exam Flashcard

Question 1:
Which one of the following code fragments will generate the given output?

Expected output:
        [[ 1.+0.j  0.+0.j  0.+0.j  0.+0.j]
        [ 0.+0.j -1.+0.j  0.+0.j  0.+0.j]
        [ 0.+0.j  0.+0.j  1.+0.j  0.+0.j]
        [ 0.+0.j  0.+0.j  0.+0.j -1.+0.j]]

Choices:
        a. p = Pauli('IZ');  print(p.to_matrix())
        b. p = Pauli('-II'); print(p.to_matrix())
        c. p = Pauli('-ZI'); print(p.to_matrix())
        d. p = Pauli('ZZ');  print(p.to_matrix())
"""

from qiskit.quantum_info.operators import Pauli

# Test each choice by constructing Pauli operators
# and printing their matrix representations

print("Option a: Pauli('IZ') →\n", Pauli('IZ').to_matrix(), "\n")
print("Option b: Pauli('-II') →\n", Pauli('-II').to_matrix(), "\n")
print("Option c: Pauli('-ZI') →\n", Pauli('-ZI').to_matrix(), "\n")
print("Option d: Pauli('ZZ') →\n", Pauli('ZZ').to_matrix(), "\n")

"""
SUMMARY (what this shows):
        - Each Pauli string maps to a 2^n x 2^n matrix via tensor products of I, X, Y, Z.
        - Negative signs in strings like '-II' or '-ZI' introduce a global phase (-1).
        - Running all four options side by side lets you match the printed output
        against the expected matrix in the question.
"""
