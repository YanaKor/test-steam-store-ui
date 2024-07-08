from selenium import webdriver


class SingletonChrome(webdriver.Chrome):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonChrome, cls).__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'driver'):
            super().__init__(*args, **kwargs)
