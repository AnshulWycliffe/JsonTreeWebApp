
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
   ```bash
   pip install request flask
   ```
4. Run the application:
   ```bash
   python main.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000` 🌐.

## 🧑‍💻 Usage
- 🌳 View the JSON tree structure on the homepage.
- Use the API endpoints to interact with the JSON data programmatically.

## 🤝 Contributing
1. Fork the repository 🍴.
2. Create a new branch for your feature or bug fix 🌿.
3. Submit a pull request with a detailed description of your changes 🔄.

## 📜 License
This project is licensed under the MIT License.
