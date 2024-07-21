import requests

def check_url(api_key, url):
    # Google Safe Browsing API URL
    google_safebrowsing_url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    params = {
        "key": api_key  # Add the API key to the request parameters
    }
    data = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],  # Define threat types to check
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    # Send a POST request to the Google Safe Browsing API
    response = requests.post(google_safebrowsing_url, params=params, json=data)
    result = response.json()  # Parse the JSON response
    return result

# Google Safe Browsing API key and URL for testing
api_key = "your_google_safebrowsing_api_key"
url = "http://example.com"
result = check_url(api_key, url)
print(result)
