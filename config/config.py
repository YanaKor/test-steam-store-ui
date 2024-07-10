import json
import os


class Config:

    @staticmethod
    def load_config():
        current_dir_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir_path, 'config.json')
        with open(config_path, 'r') as f:
            data = json.load(f)
            return data['BASE_URL']
