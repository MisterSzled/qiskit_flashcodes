# 4.2.1 Estimator Setup
# Demonstrates initializing the Qiskit Runtime service and selecting a backend.

from qiskit_ibm_runtime import QiskitRuntimeService

# Initialize account
service = QiskitRuntimeService()

# Select least-busy backend meeting conditions:
#   - operational
#   - not a simulator
#   - at least 127 qubits
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)

print(">>> Selected backend:", backend.name)

"""
SUMMARY:
- Shows how to set up Estimator by selecting a backend.
- Steps:
        1. Import QiskitRuntimeService.
        2. Initialize service.
        3. Use least_busy() to select a backend with constraints.
        4. Print backend name.
"""