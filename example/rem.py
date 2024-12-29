import requests

url = 'http://127.0.0.1:5000/api/data/remove/wyc@db/users/User1/name'  # Provide the correct path for the selected field or node
payload = {}  # No need to send a value, just the endpoint for removal

response = requests.post(url, json=payload)
print(response.json())  # Expected output: {"message": "Data removed from some/key!"}
