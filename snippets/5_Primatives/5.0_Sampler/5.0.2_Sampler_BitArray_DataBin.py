# Flashcard 5.0.2 - Working with DataBin and BitArray results

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False)
sampler = SamplerV2(backend)

# Simple |+> state circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

isa_circuit = transpile(qc, backend=backend)

# Run sampler
job = sampler.run([isa_circuit], shots=50)
result = job.result()
pub_result = result[0]

# Access DataBin → BitArray
bit_array = pub_result.data.meas
print("Raw BitArray:", bit_array)
print("First 10 bitstrings:", bit_array.get_bitstrings()[:10])
print("Counts:", bit_array.get_counts())
print("As numpy array:", bit_array.to_numpy_array())

"""
SUMMARY:
- Shows how Sampler results are stored in DataBin objects.
- BitArray gives structured access to raw measurement data.
Steps:
        1. Build simple |+> circuit.
        2. Run with Sampler.
        3. Extract DataBin result.
        4. Convert to bitstrings, counts, numpy array.
"""
