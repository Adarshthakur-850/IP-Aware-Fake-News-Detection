import requests
import json

url = "http://127.0.0.1:8000/predict"

# Test Case 1: Fake News
payload_fake = {
    "text": "Aliens have landed in New York City and are demanding pizza.",
    "ip_address": "192.168.1.1" # Private IP, likely no reputation
}

# Test Case 2: Real News
payload_real = {
    "text": "The government passed the new infrastructure bill today after a long debate.",
    "ip_address": "8.8.8.8" # Google DNS, known IP
}

def test_prediction(payload, label):
    print(f"\n--- Testing {label} ---")
    print(f"Input: {json.dumps(payload, indent=2)}")
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Response:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    print("Sending requests to API...")
    test_prediction(payload_fake, "Fake News Scenario")
    test_prediction(payload_real, "Real News Scenario")
