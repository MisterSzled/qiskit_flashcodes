# 4.2.3 Estimator ISA Transformation
# Demonstrates converting circuits and observables into ISA form with transpiler.

from qiskit.transpiler import generate_preset_pass_manager
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import qaoa_ansatz
from qiskit_ibm_runtime import QiskitRuntimeService

# Setup
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)

# Simple observable and circuit
observable = SparsePauliOp.from_sparse_list([("ZZ", [0, 1], 1.0)], num_qubits=backend.num_qubits)
circuit = qaoa_ansatz(observable, reps=1)

# Generate transpiler pass manager
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

# Transform to ISA
isa_circuit = pm.run(circuit)
isa_observable = observable.apply_layout(isa_circuit.layout)

print(">>> ISA circuit op counts:", isa_circuit.count_ops())

"""
SUMMARY:
- Converts circuit/observable into ISA (Instruction Set Architecture) form.
- Steps:
        1. Build example observable and QAOA circuit.
        2. Create pass manager with optimization_level=1.
        3. Transpile circuit into backend-specific ISA form.
        4. Apply circuit layout to observable.
        5. Print ISA op counts.
"""
