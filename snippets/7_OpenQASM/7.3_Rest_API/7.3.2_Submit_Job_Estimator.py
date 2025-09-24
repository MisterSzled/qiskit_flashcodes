import requests
import json

BEARER_TOKEN = "<YOUR_BEARER_TOKEN>"
SERVICE_CRN = "<YOUR_INSTANCE_CRN>"

url = "https://quantum.cloud.ibm.com/api/v1/jobs"

# Example Estimator job with one circuit + one observable
payload = {
        "program_id": "estimator",      # primitive type
        "backend": "ibm_brisbane",      # target backend
        "params": {
                "pubs": [[
                        # Circuit in OpenQASM 3 string form
                        "OPENQASM 3.0; include \"stdgates.inc\"; bit[1] c; x $0; c[0] = measure $0;",
                        "Z"  # Observable
                ]],
                "options": {"dynamical_decoupling": {"enable": True}},
                "version": 2,
                "resilience_level": 1
        }
}

headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Service-CRN": SERVICE_CRN,
        "Content-Type": "application/json"
}

print("Submitting Estimator job...")
response = requests.post(url, headers=headers, data=json.dumps(payload))

print("Status:", response.status_code)
print("Job Response:", response.json())

"""
SUMMARY:
- Demonstrates submitting an Estimator job using REST API.
Steps:
        1. Construct JSON payload with program_id=estimator, backend, and pubs.
        2. Add job options (dynamical decoupling, resilience level).
        3. POST request to /jobs with headers (Bearer + Service-CRN).
        4. Print response containing job ID + metadata.
"""
