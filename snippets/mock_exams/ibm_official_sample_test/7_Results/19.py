# 19. Which two of the following pieces of information are part of the dictionary
# returned by session.details(), assuming that session is an instance of
# qiskit_ibm_runtime.Session?
#
# a. Quantum circuit depth
# b. Timestamp of the last job in the session that completed
# c. Session state
# d. Primitive options
# e. Primitive unified blocs (PUBs) in each job

from qiskit_ibm_runtime import QiskitRuntimeService, Session

# --- Conceptual demonstration ---
# In practice, you would connect to IBM Quantum and open a session:
# service = QiskitRuntimeService(channel="ibm_quantum")
# session = Session(system="ibm_nairobi", service=service)

# Here we mock the returned details dictionary to show the relevant fields:
session_details = {
        "session_id": "ABC123",
        "session_state": "ACTIVE",           # Corresponds to (c) Session state
        "last_job_timestamp": "2025-10-06T10:15:00",  # Corresponds to (b)
        "user": "greg@example.com",          # extra info
        "jobs": ["job1", "job2"]             # extra info
}

print("Mocked session.details() output:")
for key, value in session_details.items():
        print(f"{key}: {value}")

"""
SUMMARY:
- Correct answers for this exam question:
        b. Timestamp of the last job in the session that completed
        c. Session state
- session.details() returns metadata about the session, including:
    * Whether the session is active or closed (session_state)
    * When the last job finished (last_job_timestamp)
"""
