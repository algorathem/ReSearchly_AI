import requests
import json

def test_source_mode_api():
    # Test the mode toggle API
    url = "http://localhost:3000/api/source/1/mode"
    headers = {"Content-Type": "application/json"}

    test_cases = [
        {"mode": "summary"},
        {"mode": "explanation"},
        {"mode": "implementation"},
        {"mode": "invalid"}  # Should fail
    ]

    for i, test_data in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i}: Mode '{test_data['mode']}' ---")
        print(f"Request: {json.dumps(test_data, indent=2)}")

        try:
            response = requests.post(url, json=test_data, headers=headers, timeout=30)

            print(f"Status: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                print("Response keys:", list(result.keys()))
                print("Message:", result.get('message'))
                print("Mode:", result.get('mode'))
                print("Source info:", result.get('source', {}))
            else:
                error_result = response.json()
                print("Error response:", error_result.get('message'))

        except Exception as e:
            print(f"Request failed: {e}")

        print("-" * 50)

if __name__ == "__main__":
    test_source_mode_api()