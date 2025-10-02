# Flashcard 5.2.0 - Transpiling to ISA Circuits for Primitives
# Toggle between Aer simulator and IBM Quantum Runtime with USE_AER

from qiskit import QuantumCircuit, transpile
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

# --- Option flag ---
USE_AER = True  # Default = True (local Aer). Set False for IBM Quantum Runtime.

# --- Step 1: Select backend ---
if USE_AER:
        backend_name = "AerSimulator"
        backend = AerSimulator()
        # For Aer we can just use normal transpile (ISA notion is runtime-specific)
        pm = None
else:
        service = QiskitRuntimeService(channel="ibm_quantum")
        backend = service.least_busy(simulator=False)
        backend_name = backend.name
        # Runtime: preset pass manager for backend ISA transpilation
        pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

print("Selected backend:", backend_name)

# --- Step 2: Build example QAOA-like parametric circuit ---
qc = QuantumCircuit(2)
qc.h([0, 1])
qc.cx(0, 1)
qc.rz(0.5, 0)

# --- Step 3: Transpile ---
if USE_AER:
        isa_circuit = transpile(qc, backend=backend)
else:
        isa_circuit = pm.run(qc)

# --- Step 4: Compare and print ---
print("Original ops:", qc.count_ops())
print("ISA ops:", isa_circuit.count_ops())
print("\nISA circuit:\n", isa_circuit)

"""
SUMMARY:
- Shows how to obtain ISA (Instruction Set Architecture) circuits tailored to a backend.
Steps:
        1. Choose backend with USE_AER flag.
        2. Build a QAOA-like circuit.
        3. Transpile:
                * Aer → use standard transpile.
                * Runtime → use generate_preset_pass_manager for ISA form.
        4. Compare operation counts before/after.
- Notes:
  * ISA circuits match the gate set of the target backend.
  * With Aer, ISA distinction is not meaningful, but the transpile still works.
"""
