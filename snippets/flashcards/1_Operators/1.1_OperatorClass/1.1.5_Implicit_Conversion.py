# Demonstrating implicit conversion of objects into Operators.

import numpy as np
from qiskit.quantum_info import Operator

# Compose operator with a matrix directly (auto-converts to Operator)
op = Operator(np.eye(2))   # 2x2 identity operator
result = op.compose([[0, 1], [1, 0]])  # X gate as a list
print("Compose with matrix directly:\n", result.data)

"""
SUMMARY:
- Shows implicit conversion in Operator methods.
- Steps:
        1. Create an Operator (identity).
        2. Pass a raw matrix (list form) into compose().
        3. Auto-conversion produces a valid Operator result.
"""
