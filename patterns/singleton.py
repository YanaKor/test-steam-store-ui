from selenium import webdriver


class SingletonChrome:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = webdriver.Chrome(*args, **kwargs)
        return cls._instance

    # def __init__(self, *args, **kwargs):
    #     if not hasattr(self, 'driver'):
    #         super().__init__(*args, **kwargs)
