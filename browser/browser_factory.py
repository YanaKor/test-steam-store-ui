from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from support.logger import log_func


class BrowserFactory:
    log = log_func()

    def __init__(self, browser_name):
        self.browser_name = browser_name.lower()

    def create_browser(self):
        if self.browser_name == 'chrome':
            self.log.info('Chrome starts')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--window-size=1920,1080')
            return webdriver.Chrome(service=Service(), options=chrome_options)
        elif self.browser_name == 'firefox':
            self.log.info('Firefox starts')
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument('--window-size=1920,1080')
            return webdriver.Firefox(options=firefox_options)
        else:
            raise ValueError(f'Invalid browser name: {self.browser_name}')
            self.log.error(f'Invalid browser name: {self.browser_name}')
