# Flashcard 5.0.3 - Bypassing runtime error mitigations with Sampler
# Toggle between Aer simulator and IBM Quantum Runtime with USE_AER

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit_aer import AerSimulator

# --- Option flag ---
USE_AER = True  # Default = True (local Aer). Set False for IBM Quantum Runtime.

# --- Step 1: Select backend ---
if USE_AER:
        backend_name = "AerSimulator"
        backend = AerSimulator()
        # Sampler with no special kwargs for Aer
        sampler = SamplerV2(backend)
else:
        service = QiskitRuntimeService(channel="ibm_quantum")
        backend = service.least_busy(simulator=False)
        backend_name = backend.name
        # Runtime Sampler with mitigation explicitly disabled
        sampler = SamplerV2(
                backend,
                resilience={"measure_mitigation": False},  # disable measurement mitigation
                options={"resilience_level": 0},          # turn off runtime auto-mitigation
        )

print("Selected backend:", backend_name)

# --- Step 2: Build Bell state circuit ---
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# --- Step 3: Transpile ---
isa_circuit = transpile(qc, backend=backend)

# --- Step 4: Run Sampler ---
job = sampler.run([isa_circuit], shots=100)
result = job.result()
pub_result = result[0]

# --- Step 5: Print raw counts ---
print("Raw counts (no mitigation):", pub_result.data.meas.get_counts())

"""
SUMMARY:
- AerSimulator path: simple sampler, no mitigation options (not supported).
- IBM Runtime path: disables all error mitigation via resilience + options.
- Demonstrates raw results from Bell state.
"""
