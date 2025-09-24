# 6.1.1_Monitor_And_Cancel_Jobs.py
# Demonstrates how to monitor and cancel IBM Runtime jobs.

from qiskit_ibm_runtime import QiskitRuntimeService

# Connect to service
service = QiskitRuntimeService()

# Get the 10 most recent jobs on a specific backend
my_backend = "ibm_brisbane"  # replace with an available backend
jobs = service.jobs(backend_name=my_backend, limit=10)
print("Recent jobs:", jobs)

# Pick the first job
job = jobs[0]

# Monitor job details
print("Job ID:", job.job_id())
print("Job status:", job.status())

# Blocking call: waits until job is complete, then returns result
# (be cautious: this waits for completion!)
result = job.result()
print("Job result:", result)

# Cancel job if needed
# job.cancel()
# print("Job cancelled.")

"""
SUMMARY:
- Monitors and controls job lifecycle in IBM Runtime.
- Steps:
        1. Query jobs for a backend with service.jobs().
        2. Select one job instance.
        3. Inspect job_id and status.
        4. Get results via job.result() (blocking).
        5. Cancel a job with job.cancel().
"""
