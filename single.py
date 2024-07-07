from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SingletonChrome(webdriver.Chrome):
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if Singleton._instance is None:
    #         chrome_options = webdriver.ChromeOptions()
    #         chrome_options.add_argument('--window-size=1920,1080')
    #         Singleton._instance = super(Singleton, cls).__new__(cls, service=Service(), options=chrome_options)
    #     return cls._instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonChrome, cls).__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'driver'):
            super().__init__(*args, **kwargs)
