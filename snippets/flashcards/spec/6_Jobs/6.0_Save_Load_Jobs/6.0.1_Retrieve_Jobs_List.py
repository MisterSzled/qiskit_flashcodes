# 6.0.1_Retrieve_Jobs_List.py
# Demonstrates how to query IBM Runtime for past jobs.

import datetime
from qiskit_ibm_runtime import QiskitRuntimeService

# Look back 90 days
three_months_ago = datetime.datetime.now() - datetime.timedelta(days=90)

# Connect to service
service = QiskitRuntimeService()

# Retrieve jobs created in the last 90 days
jobs = service.jobs(created_after=three_months_ago)
print("First 3 jobs in last 90 days:", jobs[:3])

"""
SUMMARY:
- service.jobs() lists jobs submitted to IBM Runtime.
- Can filter by time (created_after), backend, session, state, etc.
- Steps:
        1. Import datetime + QiskitRuntimeService.
        2. Create cutoff timestamp.
        3. Query jobs using service.jobs().
        4. Inspect subset of results.
"""
