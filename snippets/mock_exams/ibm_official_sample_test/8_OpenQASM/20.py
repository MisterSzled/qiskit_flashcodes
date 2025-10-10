# 20. Which one of the following is a classical data type supported by OpenQASM 3?
#
# a. complex
# b. class
# c. char
# d. enum

# --- Example OpenQASM 3 program demonstrating a 'complex' classical variable ---
program = """
OPENQASM 3.0;
include "stdgates.inc";

// Define a complex classical variable
complex alpha = 1.0 + 0.5i;

// Use it in a quantum circuit context (conceptual, no hardware effect)
qubit[1] q;
h q[0];
"""

print("OpenQASM 3 program with a complex classical variable:\n")
print(program)

"""
SUMMARY:
        - OpenQASM 3 classical types include 'complex', 'int', 'float', 'bit', 'bool', etc.
        - In this example, 'alpha' is a complex variable (supported classical type).
        - The other options ('class', 'char', 'enum') are not supported classical types.
        - This demonstrates that 'complex' is a valid OpenQASM 3 classical data type.
"""
