import json
import yaml
import os
from typing import Any

from .loaders import load_json, load_yaml, load_env, load_toml
from .savers import save_json, save_yaml, save_toml
from .validators import validate_config
from .exceptions import ConfigLoadError, ConfigValidationError, ConfigSaveError

class ConfMaster():
    def __init__(self):
        self.config = {}

    def load_from_json(self, file_path):
        try:
            self.config.update(load_json(file_path))
        except Exception as e:
            raise ConfigLoadError(f"Error loading JSON config: {e}")

    def load_from_yaml(self, file_path):
        try:
            self.config.update(load_yaml(file_path))
        except Exception as e:
            raise ConfigLoadError(f"Error loading YAML config: {e}")

    def load_from_env(self):
        self.config.update(load_env())

    def load_from_toml(self, file_path):
        try:
            self.config.update(load_toml(file_path))
        except Exception as e:
            raise ConfigLoadError(f"Error loading TOML config: {e}")

    def get(self, key, default=None) -> Any:
        keys = key.split('.')
        value = self.config
        try:
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            return default

    def set(self, key, value):
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

    def save_to_json(self, file_path):
        try:
            save_json(file_path, self.config)
        except Exception as e:
            raise ConfigSaveError(f"Error saving JSON config: {e}")

    def save_to_yaml(self, file_path):
        try:
            save_yaml(file_path, self.config)
        except Exception as e:
            raise ConfigSaveError(f"Error saving YAML config: {e}")

    def save_to_toml(self, file_path):
        try:
            save_toml(file_path, self.config)
        except Exception as e:
            raise ConfigSaveError(f"Error saving TOML config: {e}")
