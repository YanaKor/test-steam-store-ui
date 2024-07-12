import json
import os


class Config:

    @staticmethod
    def load_config():
        current_dir_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir_path, 'config.json')
        with open(config_path, 'r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def get_config_value(key):
        config_data = Config.load_config()
        if key in config_data:
            return config_data[key]
        else:
            raise KeyError(f"Key '{key}' not found.")


