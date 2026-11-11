
import json


def save_leads(path, leads):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(leads, file, indent=4)


def load_leads(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []
