# 6.0.2_Retrieve_Specific_Job.py
# Demonstrates how to get a specific job and its results.

from qiskit_ibm_runtime import QiskitRuntimeService

# Initialize service
service = QiskitRuntimeService()

# Find most recent successful job
successful_job = next(j for j in service.jobs(limit=1000) if j.status() == "DONE")

# Get job ID
job_id = successful_job.job_id()
print("Most recent completed job ID:", job_id)

# Retrieve job by ID
retrieved_job = service.job(job_id)

# Get result object
result = retrieved_job.result()
print("Retrieved result object:", result)

"""
SUMMARY:
- service.job(job_id) retrieves a specific past job.
- Steps:
        1. Query recent jobs.
        2. Filter for successful job.
        3. Extract job_id.
        4. Fetch job using service.job().
        5. Access results via job.result().
"""
