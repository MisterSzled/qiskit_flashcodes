# 12. Which one of the following patterns, expressed in terms of array broadcasting
# primitives, is represented by the given image?
#
# Parameter Value Sets: (3, 6)
# Observables Array:   (2, 3, 1)
# Resulting EV Estimates: (2, 3, 6)
#
# a. Standard multidimensional array generalization
# b. All-to-all
# c. Extended dimensional variation
# d. Best effort broadcasting

import numpy as np

# Simulate data shapes similar to Qiskit Estimator broadcasting
param_values = np.random.rand(3, 6)     # (3,6) parameter sets
observables = np.random.rand(2, 3, 1)   # (2,3,1) observable batches

print("Parameter Value Sets shape:", param_values.shape)
print("Observables Array shape:", observables.shape)

# NumPy automatically applies broadcasting rules
# to combine these arrays into a (2,3,6) result.
result = observables * param_values  # shape → (2,3,6)

print("\nBroadcasted result shape:", result.shape)
print("Resulting Expectation Value Estimates (mock):\n", result)

"""
SUMMARY:
This demonstrates Qiskit's array broadcasting concept as used in primitives such as Estimator:
        - Parameter Value Sets (3,6) define multiple parameter sweeps.
        - Observables (2,3,1) define multiple circuits/observables over those sweeps.
        - The broadcasted result (2,3,6) shows how Qiskit pairs them dimensionally.

Each exam option refers to a pattern of broadcasting behavior used to compute
Expectation Value (EV) arrays within Qiskit Runtime Primitives.
"""
