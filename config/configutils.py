import json
import os


class ConfigUtils:
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    parent_path = os.path.dirname(current_dir_path)
    config_path = os.path.join(parent_path, 'config.json')
    test_data_path = os.path.join(parent_path, 'data', 'test_data.json')

    @staticmethod
    def load_config_data(path):
        with open(path, 'r') as f:
            return json.load(f)

    @staticmethod
    def get_config_value(key):
        config_data = ConfigUtils.load_config_data(ConfigUtils.config_path)
        if key in config_data:
            return config_data[key]
        raise KeyError(f"Key '{key}' not found.")

    @staticmethod
    def update_data(file_path):
        last_modified_file = os.path.getmtime(file_path)
        current_modified_file = os.path.getmtime(ConfigUtils.config_path)
        if current_modified_file > last_modified_file:
            ConfigUtils.data = ConfigUtils.load_config_data(file_path)
            ConfigUtils.last_modified = current_modified_file

    @staticmethod
    def get_test_data_value(key, sub_key):
        config_data = ConfigUtils.load_config_data(ConfigUtils.test_data_path)
        if key in config_data:
            if sub_key in config_data[key]:
                return config_data[key][sub_key]
            return config_data[key]
        raise KeyError(f"Key '{key}' not found.")

