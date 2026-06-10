import json
import os

DATA_FILE = "data/database.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "users": [],
            "projects": [],
            "tasks": []
        }

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {
            "users": [],
            "projects": [],
            "tasks": []
        }


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def generate_id(items, id_key):
    if not items:
        return 1

    return max(item[id_key] for item in items) + 1