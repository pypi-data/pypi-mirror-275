def validate_config(config, schema):
    for key, expected_type in schema.items():
        if key not in config:
            raise ValueError(f"Missing key in config: {key}")
        if not isinstance(config[key], expected_type):
            raise ValueError(f"Invalid type for key {key}: expected {expected_type}, got {type(config[key])}")