import json
import yaml
import os
from typing import Any

from .loaders import load_json, load_yaml, load_env
from .validators import validate_config
from .exceptions import ConfigLoadError, ConfigValidationError

class ConfMaster():
    def __init__(self):
        self.config = {}

    def load_from_json(self, file_path) -> None:
        try:
            self.config.update(load_json(file_path))
        except Exception as e:
            raise ConfigLoadError(f"Error loading JSON config: {e}")

    def load_from_yaml(self, file_path) -> None:
        try:
            self.config.update(load_yaml(file_path))
        except Exception as e:
            raise ConfigLoadError(f"Error loading YAML config: {e}")

    def load_from_env(self) -> None:
        self.config.update(load_env())

    def get(self, key, default=None) -> Any:
        keys = key.split('.')
        value = self.config
        try:
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            return default

    def set(self, key, value) -> None:
        keys = key.split('.')
        d = self.config

        for k in keys[:-1]:
            if k not in d:
                d[k] = {}

            d = d[k]
            d[keys[-1]] = value

    def validate(self, schema):
        try:
            validate_config(self.config, schema)
        except ValueError as e:
            raise ConfigValidationError(f"Configuration validation error: {e}")

    def save_to_json(self, file_path) -> None:
        try:
            with open(file_path, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            raise Exception(f"Error saving JSON config: {e}")

    def save_to_yaml(self, file_path) -> None:
        try:
            with open(file_path, 'w') as f:
                yaml.safe_dump(self.config, f, default_flow_style=False)
        except Exception as e:
            raise Exception(f"Error saving YAML config: {e}")
