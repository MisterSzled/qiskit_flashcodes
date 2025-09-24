# 6.1.3_Execution_Spans_With_Masks.py
# Demonstrates filtering Sampler data using execution span masks.

import numpy as np
from qiskit.primitives import BitArray
from qiskit_ibm_runtime import QiskitRuntimeService

# Connect to service
service = QiskitRuntimeService()

# Use most recent completed job
job = next(j for j in service.jobs(limit=10) if j.status() == "DONE")
result = job.result()
spans = result[0].metadata["execution"]["execution_spans"]

# Create a fake PUB parameter set shape (2,3)
params = np.random.uniform(size=(2, 3))
print("Parameter set shape:", params.shape)

# Get mask for first PUB in first execution span
mask = spans[0].mask(0)
print("Mask shape:", mask.shape)
print("Mask sample:", mask)

# Filter BitArray measurement results using the mask
bits = result[0].data.meas
filtered_data = BitArray(bits.array[mask], bits.num_bits)
print("Filtered data (only from first span):", filtered_data)

# Filter spans by PUB indices (e.g., PUBs 0 and 2 only)
subset_spans = spans.filter_by_pub([0, 2])
print("Filtered spans:", subset_spans)

"""
SUMMARY:
- ExecutionSpan.mask(pub_index) gives a boolean array marking shots executed in that span.
- You can filter measurement results with BitArray using the mask.
- Steps:
        1. Access spans from job result metadata.
        2. Use spans[0].mask(pub_index) to get shot-level mask.
        3. Apply mask to measurement results with BitArray.
        4. Filter spans by PUB indices with spans.filter_by_pub().
"""
