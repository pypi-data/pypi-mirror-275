import json
import yaml
from typing import Any

class ConfMaster():
    def __init__(self):
        self.config = {}

    def load_from_json(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                self.config.update(json.load(f))
        except Exception as e:
            raise Exception(f"Error loading JSON config: {e}")

    def load_from_yaml(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                self.config.update(yaml.safe_load(f))
        except Exception as e:
            raise Exception(f"Error loading YAML config: {e}")

    def get(self, key: str, default: Any=None) -> Any:
        keys = key.split('.')
        value = self.config
        try:
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            return default

    def set(self, key: str, value: Any) -> None:
        keys = key.split('.')
        d = self.config

        for k in keys[:-1]:
            if k not in d:
                d[k] = {}

            d = d[k]
            d[keys[-1]] = value

    def save_to_json(self, file_path: str) -> None:
        try:
            with open(file_path, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            raise Exception(f"Error saving JSON config: {e}")

    def save_to_yaml(self, file_path: str) -> None:
        try:
            with open(file_path, 'w') as f:
                yaml.safe_dump(self.config, f, default_flow_style=False)
        except Exception as e:
            raise Exception(f"Error saving YAML config: {e}")