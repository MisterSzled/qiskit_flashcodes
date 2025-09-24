import requests
import json

BEARER_TOKEN = "<YOUR_BEARER_TOKEN>"
SERVICE_CRN = "<YOUR_INSTANCE_CRN>"

url = "https://quantum.cloud.ibm.com/api/v1/sessions"

payload = {
        "mode": "dedicated",   # session mode
        "max_ttl": 28800       # max session lifetime in seconds (8 hours)
}

headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Service-CRN": SERVICE_CRN,
        "Content-Type": "application/json"
}

print("Creating session...")
response = requests.post(url, headers=headers, data=json.dumps(payload))

session_data = response.json()
print("Session response:", session_data)

session_id = session_data.get("id")
print("\nSession ID:", session_id)

"""
SUMMARY:
- Demonstrates how to create a runtime session via REST API.
Steps:
        1. POST request to /sessions with session config (mode, TTL).
        2. Include headers (Bearer + Service-CRN).
        3. Parse JSON response to retrieve session_id.
        4. Print session ID (used in subsequent jobs).
"""
