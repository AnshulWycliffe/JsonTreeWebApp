import requests

response = requests.post('http://127.0.0.1:5000/api/data/reset')
print(response.json())  # Expected output: {"message": "Database reset!"}
