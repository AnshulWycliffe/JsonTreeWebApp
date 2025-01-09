from flask import Flask, render_template, jsonify, request
import json
import os
#import webview

app = Flask(__name__)
#window = webview.create_window("WyDBase",app,fullscreen=True,text_select=True,zoomable=True)
# Load JSON data from the file
def load_json():
    if not os.path.exists("database.json"):
        # If database.json doesn't exist, create an empty database
        save_json({"wyc@db":{}})
    with open("database.json", "r") as file:
        return json.load(file)

# Save JSON data to the file
def save_json(data):
    with open("database.json", "w") as file:
        json.dump(data, file, indent=4)

# Helper function to set data at a specific path
def set_data_at_path(data, path, value):
    keys = path.split('/')
    for key in keys[:-1]:
        data = data.setdefault(key, {})  # Create nested dictionaries if they don't exist
    if isinstance(data, dict):
        data[keys[-1]] = value  # Set the value at the final key
    else:
        return {"error": f"Cannot set value at {path}, invalid structure!"}

# Helper function to append data to a list
def append_data_at_path(data, path, value):
    keys = path.split('/')
    target_data = data

    for key in keys[:-1]:
        target_data = target_data.setdefault(key, {})

    if isinstance(target_data, list):
        # Append to a list
        target_data.append(value)
    elif isinstance(target_data, dict):
        # If the target data is a dictionary and the last key exists, update it
        key = keys[-1]
        if key in target_data:
            # If it's an existing dictionary, merge the data
            target_data[key].update(value)
        else:
            # If it's a new key, add the new value
            target_data[key] = value
    else:
        return {"error": f"Cannot append data at {path}, target is neither a list nor a dictionary!"}

    return None  # No error, everything worked fine


@app.route('/')
def home():
    data = load_json()
    return render_template('index.html', data=data)

@app.route('/api/data', methods=['GET'])
def print_data():
    data = load_json()
    return jsonify(data)

@app.route('/api/data/set/<path:subpath>', methods=['POST'])
def set_data(subpath):
    new_data = request.get_json()  # Get data from the POST request
    value = new_data.get("value", {})
    data = load_json()

    result = set_data_at_path(data, subpath, value)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400

    save_json(data)
    return jsonify({"message": f"Data set at {subpath}!"}), 201

@app.route('/api/data/append/<path:subpath>', methods=['POST'])
def append_data(subpath):
    new_data = request.get_json()  # Get data from the POST request
    value = new_data.get("value", {})
    data = load_json()

    result = append_data_at_path(data, subpath, value)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400

    save_json(data)
    return jsonify({"message": f"Data appended at {subpath}!"}), 201

@app.route('/api/data/get/<path:subpath>', methods=['GET'])
def get_data(subpath):
    data = load_json()
    keys = subpath.split('/')
    for key in keys:
        if key in data:
            data = data[key]
        else:
            return jsonify({"error": f"{subpath} not found!"}), 404
    return jsonify(data), 200

@app.route('/api/data/remove/<path:subpath>', methods=['POST'])
def remove_data(subpath):
    data = load_json()
    keys = subpath.split('/')
    target_data = data
    for key in keys[:-1]:
        if key in target_data:
            target_data = target_data[key]
        else:
            return jsonify({"error": f"{subpath} not found!"}), 404

    # Remove the data at the final key
    if keys[-1] in target_data:
        del target_data[keys[-1]]
        save_json(data)
        return jsonify({"message": f"Data removed from {subpath}!"}), 200
    else:
        return jsonify({"error": f"{subpath} not found!"}), 404

# Route to reset the database (for testing purposes)
@app.route('/api/data/reset', methods=['POST'])
def reset_data():
    save_json({"wyc@db":{}})
    return jsonify({"message": "Database reset!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
    #webview.start()