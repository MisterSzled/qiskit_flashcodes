# 4.2.6 Backend Primitives
# Demonstrates using generic backend primitives (not Runtime service).

from qiskit.primitives import BackendEstimatorV2, BackendSamplerV2
# Replace with actual provider import, e.g.:
# from qiskit_ibm_provider import IBMProvider
# provider = IBMProvider()

# Example placeholder: assume provider instance exists
# backend = provider.get_backend('backend_name')

# Initialize primitives with backend
# estimator = BackendEstimatorV2(backend)
# sampler = BackendSamplerV2(backend)

print(">>> BackendEstimatorV2 and BackendSamplerV2 follow same PUB format as Runtime primitives")
print(">>> Differences: no built-in error mitigation, requires backend memory support for Sampler")

"""
SUMMARY:
- Shows how to use backend primitives (local, generic).
- Steps:
        1. Import BackendEstimatorV2 and BackendSamplerV2.
        2. Get backend from a provider.
        3. Initialize primitives with backend.
        4. Note differences vs Runtime primitives:
                - No built-in mitigation.
                - Sampler requires backend memory support.
"""
