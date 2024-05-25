import json
import yaml
import os
import toml


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def load_env():
    return {key: value for key, value in os.environ.items()}

def load_toml(file_path):
    with open(file_path, 'r') as f:
        return toml.load(f)