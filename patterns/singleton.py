from selenium import webdriver


class Browser:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = webdriver.Chrome(*args, **kwargs)
        return cls._instance

    @classmethod
    def quit(cls):
        cls._instance.quit()
        cls._instance = None
