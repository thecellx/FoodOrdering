import json
import os


class Config:
    _CONFIG_PATH = "config/food_ordering.json"
    _config: dict = None

    def __init__(self):
        # If the configuration has already been loaded we have nothing to do
        if Config._config:
            return

        assert os.path.exists(Config._CONFIG_PATH), f"Config file does not exist at {Config._CONFIG_PATH}"
        with open(Config._CONFIG_PATH) as f:
            Config._config = json.load(f)

    @staticmethod
    def get(config_param):
        assert config_param in Config._config, f"'{config_param}' is missing from configuration"
        return Config._config[config_param]
