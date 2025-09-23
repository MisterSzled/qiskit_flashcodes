# 4.2.2 Estimator Circuit and Observable
# Demonstrates building a circuit and observable for the Estimator primitive.

from qiskit.circuit.library import qaoa_ansatz
from qiskit.quantum_info import SparsePauliOp

# Assume backend from previous step
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)

# Define observable using coupling map edges
entanglement = [tuple(edge) for edge in backend.coupling_map.get_edges()]
observable = SparsePauliOp.from_sparse_list(
        [("ZZ", [i, j], 0.5) for i, j in entanglement],
        num_qubits=backend.num_qubits,
)

# Build parametrized QAOA circuit
circuit = qaoa_ansatz(observable, reps=2)

# Example parameter values for execution
param_values = [0.1, 0.2, 0.3, 0.4]

print(">>> Observable defined with ZZ terms")
print(">>> First few Pauli strings:", observable.paulis[:5])

"""
SUMMARY:
- Builds inputs for Estimator primitive.
- Steps:
        1. Import QAOA ansatz and SparsePauliOp.
        2. Extract backend coupling map edges.
        3. Define ZZ observable across those edges.
        4. Build QAOA ansatz circuit with reps=2.
        5. Assign example parameter values for later execution.
"""
