import json
import os


class ConfigUtils:
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
    with open(config_path, 'r') as f:
        data = json.load(f)

    @staticmethod
    def get_config_value(key):
        config_data = ConfigUtils.data
        if key in config_data:
            return config_data[key]
        raise KeyError(f"Key '{key}' not found.")

    @staticmethod
    def update_data(file_path):
        last_modified_file = os.path.getmtime(file_path)
        current_modified_file = os.path.getmtime(ConfigUtils.config_path)
        if current_modified_file > last_modified_file:
            with open(file_path, 'r') as f:
                return json.load(f)
