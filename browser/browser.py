from browser.browser_factory import BrowserFactory
from support.logger import log_func


class Browser:
    log = log_func()

    def __init__(self, browser_name):
        self.browser = BrowserFactory(browser_name)
        self.driver = self.browser.create_browser()

    def get(self, url):
        self.log.info(f'Opening page {url}')
        self.driver.get(url)

    def quit(self):
        self.log.info('Closing the browser')
        self.driver.quit()
