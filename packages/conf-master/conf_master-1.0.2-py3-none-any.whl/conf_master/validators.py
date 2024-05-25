def validate_config(config, schema):
    for key, expected_type in schema.items():
        keys = key.split(".")
        value = config
        for k in keys:
            if k not in value:
                raise ValueError(f"Missing key in config: {key}")
            value = value[k]
        if not isinstance(value, expected_type):
            raise ValueError(
                f"Invalid type for key {key}: expected {expected_type}, got {type(value)}"
            )
