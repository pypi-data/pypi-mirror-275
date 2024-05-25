import json
import os
import yaml

def load_json(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                self.config.update(json.load(f))
        except Exception as e:
            raise Exception(f"Error loading JSON config: {e}")

def load_yaml(self, file_path: str) -> None:
    try:
        with open(file_path, 'r') as f:
            self.config.update(yaml.safe_load(f))
    except Exception as e:
        raise Exception(f"Error loading YAML config: {e}")

def load_env(self) -> None:
    for key, value in os.environ.items():
        self.config[key] = value