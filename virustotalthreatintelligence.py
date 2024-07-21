import requests

def check_virustotal(api_key, file_hash):
    # Construct the URL for the VirusTotal API
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "x-apikey": api_key  # Add the API key to the request headers
    }

    # Send a GET request to the VirusTotal API
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # If the request is successful, return the response data
        data = response.json()
        return data
    else:
        # If the request fails, return None
        return None

# VirusTotal API key and file hash for testing
api_key = "your_virustotal_api_key"
# Example File Hash
file_hash = "44d88612fea8a8f36de82e1278abb02f"
result = check_virustotal(api_key, file_hash)
print(result)
