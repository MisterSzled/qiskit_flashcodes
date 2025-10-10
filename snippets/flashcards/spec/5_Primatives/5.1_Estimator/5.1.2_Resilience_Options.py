# Flashcard 5.1.2 - EstimatorV2 with Resilience Options
# Toggle between Aer simulator and IBM Quantum Runtime with USE_AER

from qiskit.circuit.library import real_amplitudes
from qiskit.quantum_info import SparsePauliOp
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2
from qiskit_aer import AerSimulator
import numpy as np

# --- Option flag ---
USE_AER = True  # Default = True (run locally on Aer). Set to False for IBM Quantum Runtime.

# --- Step 1: Select backend ---
if USE_AER:
        backend_name = "AerSimulator"
        backend = AerSimulator()
else:
        service = QiskitRuntimeService(channel="ibm_quantum")
        backend = service.least_busy(simulator=False)
        backend_name = backend.name

print("Selected backend:", backend_name)

# --- Step 2: Build a simple variational ansatz (RealAmplitudes)
qc = real_amplitudes(num_qubits=2, reps=1)

# Observable: Z⊗Z
observable = SparsePauliOp.from_list([("ZZ", 1.0)])

# --- Step 3: Transpile + align observable layout (best-effort) ---
isa_circuit = transpile(qc, backend=backend)
# Try applying the circuit layout to the observable if supported; otherwise keep observable
try:
        isa_observable = observable.apply_layout(isa_circuit.layout)
except Exception:
        isa_observable = observable

# --- Step 4: Initialize EstimatorV2 (only add resilience/options for runtime backends) ---
if USE_AER:
        estimator = EstimatorV2(backend)
else:
        estimator = EstimatorV2(
                backend,
                resilience={"measure_mitigation": True},  # enable measurement error mitigation
                options={"resilience_level": 1},          # higher levels = stronger mitigation
        )

# --- Step 5: Run with a single random parameter set ---
params = np.random.rand(qc.num_parameters)

job = estimator.run([(isa_circuit, isa_observable, [params])])
result = job.result()[0]

# --- Step 6: Print results ---
# Note: result.data.evs shape may vary by API version; this mirrors typical usage.
print("\nExpectation value(s):", result.data.evs)
print("Metadata:", getattr(result, "metadata", None))

"""
SUMMARY:
- Demonstrates setting resilience options in EstimatorV2 conditionally.
Steps:
        1. Choose backend with USE_AER flag.
        2. Build variational circuit (real_amplitudes).
        3. Define observable ZZ and attempt to align layout.
        4. Initialize EstimatorV2 without runtime-only kwargs for Aer; with resilience for IBM Runtime.
        5. Run estimator and retrieve expectation values + metadata.
- Notes:
        * Passing runtime-only kwargs (resilience/options) to EstimatorV2 when using Aer raises a TypeError.
        * This snippet avoids that by applying those kwargs only for real IBM Runtime backends.
"""
