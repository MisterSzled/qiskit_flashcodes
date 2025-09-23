# 1.0.4 Operator Subsystem Dimensions
# Demonstrates how Operator tracks and customizes subsystem dimensions.

import numpy as np
from qiskit.quantum_info.operators import Operator

# ===== Basic Example: 1-qubit to 1-qubit (square matrix) =====
# A 1-qubit operator is a 2x2 square matrix
basic_op_matrix = np.array([[0, 1],
                        [1, 0]])  # Pauli-X gate
op_basic = Operator(basic_op_matrix)
print("Basic 1-qubit operator (Pauli-X):")
print(op_basic)
print("Input dimensions:", op_basic.input_dims())   # [2] → 1 qubit
print("Output dimensions:", op_basic.output_dims()) # [2] → 1 qubit
print()

# ===== Example: 1-qubit input, 2-qubit output (rectangular) =====
# Non-square, just for demonstration of input/output dims
op = Operator(np.random.rand(2**1, 2**2))
print("Operator with input 1-qubit, output 2-qubit (rectangular):")
print(op)
print("Input dimensions:", op.input_dims())   # [2] → 1 qubit
print("Output dimensions:", op.output_dims()) # [4] → 2 qubits
print()

# ===== Example: 6x6 matrix (doesn't divide into qubits → single system) =====
op = Operator(np.random.rand(6, 6))
print("Operator with 6x6 matrix:")
print("Input dimensions:", op.input_dims())   # [6] → single 6-level system
print("Output dimensions:", op.output_dims()) # [6]
print()

# ===== Force dimensions manually: input treated as 4-level system =====
op = Operator(np.random.rand(2**1, 2**2), input_dims=[4])
print("Forced input dimension (4-level system):")
print("Input dimensions:", op.input_dims())
print("Output dimensions:", op.output_dims())
print()

# ===== Example: composite system (qubit + qutrit) =====
op = Operator(np.random.rand(6, 6), input_dims=[2, 3], output_dims=[2, 3])
print("Operator with qubit + qutrit subsystem:")
print("Input dimensions:", op.input_dims())
print("Output dimensions:", op.output_dims())
print()

# Extract subsystem dimensions
print("Dimension of input system 0:", op.input_dims([0]))
print("Dimension of input system 1:", op.input_dims([1]))

"""
SUMMARY:
- Demonstrates how Operator tracks subsystem dimensions.
- Steps:
        1. Start with a basic 1-qubit operator (Pauli-X) to understand square operators.
        2. Observe input/output dims for non-square operator (1→2 qubits).
        3. Initialize larger square matrices (6x6) → single system.
        4. Override input dimensions manually for multi-level systems.
        5. Define composite systems (e.g., qubit+qutrit).
        6. Extract dimensions of individual subsystems.
"""
