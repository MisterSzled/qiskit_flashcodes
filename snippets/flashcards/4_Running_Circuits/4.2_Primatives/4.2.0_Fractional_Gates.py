# 4.2.0 Fractional Gates
# Demonstrates how to request a backend that supports experimental fractional gates.

from qiskit_ibm_runtime import QiskitRuntimeService

# Initialize the service (assumes account already set up)
service = QiskitRuntimeService()

# Request a backend that supports fractional gates
fractional_backend = service.least_busy(use_fractional_gates=True)

print(">>> Fractional gate backend selected:", fractional_backend.name)

"""
SUMMARY:
- Shows how to request a backend with fractional gate support.
- Steps:
        1. Import QiskitRuntimeService.
        2. Initialize the service (uses stored IBM Quantum credentials).
        3. Call least_busy() with use_fractional_gates=True.
        4. Print the selected backend name.
"""