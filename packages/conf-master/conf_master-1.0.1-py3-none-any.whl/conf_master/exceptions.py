class ConfigError(Exception):
    """Base class for configuration related errors."""
    pass


class ConfigLoadError(ConfigError):
    """Raised when there is an error loading the configuration."""
    pass


class ConfigValidationError(ConfigError):
    """Raised when the configuration validation fails."""
    pass
