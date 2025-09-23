# 1.0.4 Operator Subsystem Dimensions
# Demonstrates how Operator tracks and customizes subsystem dimensions.

import numpy as np
from qiskit.quantum_info.operators import Operator

# Example: 1-qubit input, 2-qubit output (randomized matrix)
op = Operator(np.random.rand(2**1, 2**2))
print("Operator with input 1-qubit, output 2-qubit:")
print("Input dimensions:", op.input_dims())
print("Output dimensions:", op.output_dims())
print()

# Example: 6x6 matrix (doesn't divide into qubits → single system)
op = Operator(np.random.rand(6, 6))
print("Operator with 6x6 matrix:")
print("Input dimensions:", op.input_dims())
print("Output dimensions:", op.output_dims())
print()

# Force dimensions manually: input treated as 4-level system
op = Operator(np.random.rand(2**1, 2**2), input_dims=[4])
print("Forced input dimension (4-level system):")
print("Input dimensions:", op.input_dims())
print("Output dimensions:", op.output_dims())
print()

# Example: composite system (qubit + qutrit)
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
        1. Initialize operator with random matrices.
        2. Observe default inferred subsystem dims.
        3. Override input dims manually.
        4. Define composite systems (e.g., qubit+qutrit).
        5. Extract dimensions of individual subsystems.
"""
