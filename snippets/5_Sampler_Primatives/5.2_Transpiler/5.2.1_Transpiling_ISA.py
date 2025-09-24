# Flashcard 5.2.0 - Transpiling to ISA Circuits for Primitives

from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False)

# Example: QAOA-like circuit (parameterized)
qc = QuantumCircuit(2)
qc.h([0, 1])
qc.cx(0, 1)
qc.rz(0.5, 0)

# Use preset pass manager for backend-specific transpilation
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pm.run(qc)

print("Original ops:", qc.count_ops())
print("ISA ops:", isa_circuit.count_ops())
print("\nISA circuit:\n", isa_circuit)

"""
SUMMARY:
- Demonstrates generating ISA circuits with backend-specific transpiler.
Steps:
        1. Build sample parametric circuit.
        2. Create pass manager with `generate_preset_pass_manager`.
        3. Transpile to ISA form.
        4. Compare operation counts before/after.
"""
