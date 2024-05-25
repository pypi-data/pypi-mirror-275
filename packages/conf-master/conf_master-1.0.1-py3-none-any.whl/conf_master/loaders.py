import json
import yaml
import os


def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"Error loading JSON config: {e}")


def load_yaml(file_path):
    try:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise Exception(f"Error loading YAML config: {e}")


def load_env():
    return {key: value for key, value in os.environ.items()}
