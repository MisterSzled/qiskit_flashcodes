import requests

# Replace with your actual IBM Cloud API key
API_KEY = "MY_APIKEY"

# Endpoint to request a bearer token using your API key
url = "https://iam.cloud.ibm.com/identity/token"

# Data payload for IAM API
data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": API_KEY
}

# Required header for the token request
headers = {"Content-Type": "application/x-www-form-urlencoded"}

print("Requesting bearer token...")
response = requests.post(url, data=data, headers=headers)

# Parse token response
token_data = response.json()
print("Response:", token_data)

bearer_token = token_data.get("access_token")
print("\nYour bearer token is:", bearer_token)

"""
SUMMARY:
- Demonstrates how to authenticate with IBM Cloud IAM to obtain a bearer token.
Steps:
        1. Define IAM endpoint + API key.
        2. Send POST request with grant_type + apikey.
        3. Parse JSON response to extract access_token.
        4. Print token (valid for ~1 hour).
"""
