import re
from pymongo import MongoClient
from flask import Flask, jsonify, request

automation_configuration = Flask(__name__)
# MongoDB connection
myclient = MongoClient("mongodb+srv://devendra8182_db_user:h7bjVagR8ru8DFdo@devendra.io1nvag.mongodb.net/")
mydb = myclient["mongo_db_practice"]
mycol = mydb["system_config"]

# ---------------- Parsing Config File ----------------
def parse_config_string(file_path):
    try:
        with open("E:\Devops_Course\Python\Assignments\configuration.txt", "r") as filename:
            lines = filename.readlines()
        config_data = {}
        current_section = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if "=" not in line:  # Section
                current_section = line.strip("[]")
                config_data[current_section] = {}
            else:  # Key-value pair
                if current_section:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    if value.isdigit():
                        value = int(value)
                    config_data[current_section][key] = value
        return config_data
        print (config_data)
    except FileNotFoundError:
        print("Error: File not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

# ---------------- Flatten & Insert into MongoDB ----------------
def save_to_mongo(config):
    for section, settings in config.items():
        for key, value in settings.items():
            doc_key = f"{section.lower()}_{key}"
            mycol.update_one(
                {"key": doc_key},                     # find by key
                {"$set": {"key": doc_key, "value": value}},  # update value
                upsert=True                           # insert if not found
            )

# ---------------- Display Data ----------------
def display_config(config_data):
    if not config_data:
        print("Warning: Configuration data is empty.")
        return
    print("Extracted Configuration Data:")
    print("=" * 40)
    for section, settings in config_data.items():
        print(f"\n{section}:")
        for key, value in settings.items():
            print(f"  {key} = {value}")

# ---------------- Flask API ----------------
@automation_configuration.route("/search", methods=["GET"])
def user_search():
    user_input = request.get_json()
    query_text = user_input.get("query", "")

    matches = re.findall(r"database|server|user", query_text, re.IGNORECASE)

    if not matches:
        return jsonify({"error": "Invalid section"}), 400

    section = matches[0].lower()
    results = mycol.find(
        {"key": {"$regex": f"^{section}_"}}, {"_id": 0}
    )

    user_search = {doc["key"]: doc["value"] for doc in results}
    return jsonify(user_search)


if __name__ == "__main__":
    path = "configuration.txt"  # safer path
    config = parse_config_string(path)
    display_config(config)

    if config:
        save_to_mongo(config)
        print("Configuration saved in MongoDB.")

    automation_configuration.run(debug=True)
