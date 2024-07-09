import json
import os


class Config:

    def __init__(self, config_file):
        self.config_file = config_file

    def load_config(self):
        config_path = os.path.join(os.getcwd(), self.config_file)
        with open(config_path, 'r') as f:
            data = json.load(f)
            return data['BASE_URL']
