import requests
import json

BEARER_TOKEN = "<YOUR_BEARER_TOKEN>"
SERVICE_CRN = "<YOUR_INSTANCE_CRN>"
SESSION_ID = "<YOUR_SESSION_ID>"   # from previous flashcard

url = "https://quantum.cloud.ibm.com/api/v1/jobs"

# Example sampler job inside a session
payload = {
        "program_id": "sampler",
        "backend": "ibm_brisbane",
        "session_id": SESSION_ID,   # attach job to existing session
        "params": {
                "pubs": [[
                        "OPENQASM 3.0; include \"stdgates.inc\"; bit[1] c; x $0; c[0] = measure $0;"
                ]],
                "options": {},
                "version": 2
        }
}

headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Service-CRN": SERVICE_CRN,
        "Content-Type": "application/json"
}

print("Submitting Sampler job inside session...")
response = requests.post(url, headers=headers, data=json.dumps(payload))

print("Status:", response.status_code)
print("Job Response:", response.json())

"""
SUMMARY:
- Demonstrates submitting a Sampler job tied to a session.
Steps:
        1. Use session_id in payload to link job to active session.
        2. Construct payload with program_id=sampler and pubs.
        3. Send POST request to /jobs with headers.
        4. Print job response (job_id + execution info).
"""
