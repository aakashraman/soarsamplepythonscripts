import re

def extract_indicators(email_text):
    # Define regex patterns for IP addresses, URLs, and email addresses
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches in the email text
    ips = re.findall(ip_pattern, email_text)
    urls = re.findall(url_pattern, email_text)
    emails = re.findall(email_pattern, email_text)

    # Return the results in a dictionary
    return {
        'IPs': ips,
        'URLs': urls,
        'Emails': emails
    }

# Example email text for testing
email_text = """Example email text with an IP 192.168.1.1, a URL http://example.com, and an email address example@example.com."""
indicators = extract_indicators(email_text)
print(indicators)
