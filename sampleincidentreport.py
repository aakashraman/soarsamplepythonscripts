import json

def generate_incident_report(incident_details):
    # Create a report dictionary with incident details
    report = {
        "incident_id": incident_details.get("incident_id"),
        "date": incident_details.get("date"),
        "summary": incident_details.get("summary"),
        "indicators": incident_details.get("indicators"),
        "actions_taken": incident_details.get("actions_taken"),
        "status": incident_details.get("status"),
        "next_steps": incident_details.get("next_steps")
    }

    # Convert the report dictionary to a JSON string with indentation
    return json.dumps(report, indent=4)

# Example incident details for testing
incident_details = {
    "incident_id": "INC123456",
    "date": "2024-07-21",
    "summary": "Phishing email detected and blocked.",
    "indicators": {
        "IPs": ["192.168.1.1"],
        "URLs": ["http://example.com"],
        "Emails": ["phisher@example.com"]
    },
    "actions_taken": ["Blocked IP", "Reported URL to Google Safe Browsing"],
    "status": "Resolved",
    "next_steps": ["Monitor for similar emails", "Educate users on phishing"]
}

report = generate_incident_report(incident_details)
print(report)
