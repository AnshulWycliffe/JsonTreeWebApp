import requests

response = requests.get('http://127.0.0.1:5000/api/data/get/wyc@db/users/User1')
print(response.json())  # This will print the value at the path "some/key"
