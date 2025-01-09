
# 🌳 JSON Tree Viewer and Editor

## 🛠️ Overview
This project is a full-stack web application for managing JSON data. It allows users to:
- 📜 View JSON data in a collapsible tree format.
- ✏️ Edit JSON data using a Flask API backend.
- 🔄 Update single or multiple fields dynamically.

### 💻 Technologies Used
- **Backend**: Python Flask 🐍
- **Frontend**: HTML, CSS, JavaScript 🌐
- **Database**: JSON file-based storage 🗂️

## ✨ Features
1. **Tree Viewer**: Displays JSON data as a collapsible tree structure 🌲.
2. **Edit Functionality**:
   - 📝 Update single or multiple fields of JSON data.
   - ➕ Append or ➖ Remove data dynamically.
3. **API Endpoints**:
   - 📥 `/api/data` - Retrieve all data.
   - 🔍 `/api/data/get/wyc@db/<path>` - Get data at a specific path.
   - ✏️ `/api/data/append/wyc@db/<path>` - Append data at a specific path.
   - 🛠️ `/api/data/set/wyc@db/<path>` - Update a single or multiple field of a node.
   - ❌ `/api/data/remove/wyc@db/<path>` - Remove a single or multiple fields of a node.
   - ❌ `/api/data/reset` - Reset database.

## 🧑‍💻 Operations
1. Set Only One Field
   ```python
   import requests
   url = 'http://127.0.0.1:5000/api/data/set/wyc@db/users/User1/name'
   payload = {"value": "John Doe"}

   response = requests.post(url, json=payload)
   print(response.json())  # Expected output: {"message": "Data set at some/key!"}
   ```
2. Append Data
   ```python
   import requests

   url = 'http://127.0.0.1:5000/api/data/append/wyc@db/users'
   payload = {
       "value": {
           "User2": {"name": "John Doe Part 2", "age": 12}
       }
   }

   response = requests.post(url, json=payload)
   print(response.json())  # Expected output: {"message": "Data appended at some/users!"}
   ```
3. Fetch All Data
   ```python
   import requests
   response = requests.get('http://127.0.0.1:5000/api/data')
   print(response.json())
   ```
4. Fetch Selected Data
   ```python
   import requests

   response = requests.get('http://127.0.0.1:5000/api/data/get/wyc@db/users/User1')
   print(response.json())  # This will print the value at the path "some/key"
   ```

5. Remove Data
   ```python
   import requests

   url = 'http://127.0.0.1:5000/api/data/remove/wyc@db/users/User1/name'  # Provide the correct path for the selected field or node
   payload = {}  # No need to send a value, just the endpoint for removal

   response = requests.post(url, json=payload)
   print(response.json())  # Expected output: {"message": "Data removed from some/key!"}
   ```

6. Reset Database
   ```python
   import requests

   response = requests.post('http://127.0.0.1:5000/api/data/reset')
   print(response.json())  # Expected output: {"message": "Database reset!"}
   ```

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AnshulWycliffe/JsonTreeWebApp
   ```
2. Navigate to the project directory:
   ```bash
   cd json-tree-viewer
   ```
3. Install dependencies:
   ```python
   pip install request flask
   ```
4. Run the application:
   ```python
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000` 🌐.

## 🧑‍💻 Usage
- 🌳 View the JSON tree structure on the homepage.
- ![image](https://github.com/user-attachments/assets/4566ab72-8b71-4644-b36c-bb0ba4e026ca)
- Use the API endpoints to interact with the JSON data programmatically.

## 🤝 Contributing
1. Fork the repository 🍴.
2. Create a new branch for your feature or bug fix 🌿.
3. Submit a pull request with a detailed description of your changes 🔄.

## 📜 License
This project is licensed under the MIT License.
