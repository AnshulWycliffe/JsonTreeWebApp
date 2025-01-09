import requests
url = 'http://127.0.0.1:5000/api/data/set/wyc@db/users/User1/name'
payload = {"value": "John Doe"}

response = requests.post(url, json=payload)
print(response.json())  # Expected output: {"message": "Data set at some/key!"}
