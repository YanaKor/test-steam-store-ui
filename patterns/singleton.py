from selenium import webdriver


class Browser:
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         # cls._instance = super(Browser, cls).__new__(cls)
    #         cls._instance.driver = webdriver.Chrome(*args, **kwargs)
    #     return cls._instance
    #
    # def get(self, url):
    #     self.driver.get(url)

    # def quit(self):
    #     self.driver.quit()
    #     Browser._instance = None
    #
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = webdriver.Chrome(*args, **kwargs)
        return cls._instance

    # def quit(self):
    #     if self.driver:
    #         self.driver.quit()
    #         Browser._instance = None
