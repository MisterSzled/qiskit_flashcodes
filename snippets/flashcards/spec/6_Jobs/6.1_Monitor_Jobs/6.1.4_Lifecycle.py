# 6.4_JobLifecycleDemo.py
# Demonstrates a full job lifecycle: submit, monitor, cancel, and inspect spans.

import numpy as np
from qiskit.circuit.library import RealAmplitudes
from qiskit.primitives import SamplerV2, BitArray
from qiskit_ibm_runtime import QiskitRuntimeService

# Step 1. Initialize service
service = QiskitRuntimeService()

# Step 2. Build a test circuit + sampler
circuit = RealAmplitudes(2)
sampler = SamplerV2()

# Step 3. Submit job
job = sampler.run([(circuit, None, np.random.uniform(size=(2, 3)))])
print("Submitted job ID:", job.job_id())

# Step 4. Monitor job
print("Job status:", job.status())
result = job.result()
print("Job result keys:", list(result.keys()))

# Step 5. Inspect execution spans
spans = result.metadata["execution"]["execution_spans"]
print("Number of spans:", len(spans))
print("First span start:", spans[0].start, "end:", spans[0].stop)

# Example of filtering data by span mask
mask = spans[0].mask(0)  # mask for first PUB
bits = result[0].data.meas
filtered = BitArray(bits.array[mask], bits.num_bits)
print("Filtered BitArray size:", filtered.array.shape)

# Step 6. Cancel (only if still running; may no-op if completed fast)
try:
        job.cancel()
        print("Job cancelled (or already finished).")
except Exception:
        print("Job could not be cancelled (likely finished).")

"""
SUMMARY:
        - Submit → job = sampler.run([...]).
        - Monitor → job.status(), job.result().
        - Inspect execution spans → result.metadata["execution"]["execution_spans"].
        - Filter results via BitArray + mask.
        - Cancel → job.cancel() (if still active).
"""
