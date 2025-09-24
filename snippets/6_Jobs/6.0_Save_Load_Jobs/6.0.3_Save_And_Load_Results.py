# 6.0.3_Save_And_Load_Results.py
# Demonstrates saving job results to disk and reloading later.

import json
from qiskit_ibm_runtime import QiskitRuntimeService, RuntimeEncoder, RuntimeDecoder

# Connect to service
service = QiskitRuntimeService()

# Get last successful job for demonstration
successful_job = next(j for j in service.jobs(limit=1000) if j.status() == "DONE")
result = successful_job.result()

# Save result to JSON file
with open("result.json", "w") as file:
        json.dump(result, file, cls=RuntimeEncoder)
print("Result saved to result.json")

# Load result back from JSON
with open("result.json", "r") as file:
        loaded_result = json.load(file, cls=RuntimeDecoder)

print("Reloaded result:", loaded_result)

"""
SUMMARY:
- Results can be persisted locally using JSON serialization.
- RuntimeEncoder / RuntimeDecoder handle Qiskit data types.
- Steps:
        1. Retrieve job result.
        2. Dump result to disk with json.dump + RuntimeEncoder.
        3. Load result later with json.load + RuntimeDecoder.
"""
