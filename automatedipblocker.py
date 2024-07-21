import requests

def block_ip(firewall_api_url, api_key, ip_address):
    headers = {
        "Authorization": f"Bearer {api_key}",  # Add the API key to the request headers
        "Content-Type": "application/json"
    }
    data = {
        "ip": ip_address,  # IP address to be blocked
        "action": "block"  # Action to be performed
    }

    # Send a POST request to the firewall API
    response = requests.post(firewall_api_url, headers=headers, json=data)
    return response.status_code, response.json()

# Firewall API URL, API key, and IP address for testing
firewall_api_url = "https://firewall.example.com/api/block"
api_key = "your_firewall_api_key"
ip_address = "192.168.1.1"
status_code, result = block_ip(firewall_api_url, api_key, ip_address)
print(status_code, result)
