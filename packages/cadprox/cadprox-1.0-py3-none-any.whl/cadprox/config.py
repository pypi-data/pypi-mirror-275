import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), '../cloudflare.json')

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        print("Configuration file not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON configuration file.")
        return None
