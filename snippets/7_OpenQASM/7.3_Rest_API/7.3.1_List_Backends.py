import requests

# Replace with your bearer token and service CRN
BEARER_TOKEN = "<YOUR_BEARER_TOKEN>"
SERVICE_CRN = "<YOUR_INSTANCE_CRN>"

url = "https://quantum.cloud.ibm.com/api/v1/backends"

headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Service-CRN": SERVICE_CRN
}

print("Fetching list of available backends...")
response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Backends JSON:", response.json())

"""
SUMMARY:
- Demonstrates how to query Qiskit Runtime REST API for available backends.
Steps:
        1. Provide Authorization header with bearer token.
        2. Provide Service-CRN header for your instance.
        3. Send GET request to /backends endpoint.
        4. Print backend list in JSON.
"""
