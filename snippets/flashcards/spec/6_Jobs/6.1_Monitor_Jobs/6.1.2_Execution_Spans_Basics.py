# 6.1.2_Execution_Spans_Basics.py
# Demonstrates how to inspect execution span metadata of a Sampler job.

from qiskit_ibm_runtime import QiskitRuntimeService

# Connect to service
service = QiskitRuntimeService()

# Retrieve most recent completed job
job = next(j for j in service.jobs(limit=10) if j.status() == "DONE")
result = job.result()

# Access execution spans from metadata
spans = result[0].metadata["execution"]["execution_spans"]
print("Execution spans object:", spans)

# Basic span info
print("Number of spans:", len(spans))
print("Start of first span:", spans.start)
print("End of last span:", spans.stop)
print("Total duration (s):", spans.duration)

"""
SUMMARY:
- Sampler results include timing info grouped in ExecutionSpans.
- ExecutionSpans track start, stop, and shot counts per span.
- Steps:
        1. Get job result.
        2. Access metadata["execution"]["execution_spans"].
        3. Explore span properties (start, stop, duration).
"""
