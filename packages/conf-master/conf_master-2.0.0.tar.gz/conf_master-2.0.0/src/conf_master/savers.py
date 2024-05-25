import json
import yaml
import toml


def save_json(file_path, config):
    with open(file_path, "w") as f:
        json.dump(config, f, indent=4)

def save_yaml(file_path, config):
    with open(file_path, "w") as f:
        yaml.safe_dump(config, f, default_flow_style=False)

def save_toml(file_path, config):
    with open(file_path, "w") as f:
        toml.dump(config, f)
