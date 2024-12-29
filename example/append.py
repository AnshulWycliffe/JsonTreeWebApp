import requests

url = 'http://127.0.0.1:5000/api/data/append/wyc@db/users'
payload = {
    "value": {
        "User2": {"name": "John Doe Part 2", "age": 12}
    }
}

response = requests.post(url, json=payload)
print(response.json())  # Expected output: {"message": "Data appended at some/users!"}
