from support.logger import log_func
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement:
    DEFAULT_TIMEOUT = 10
    log = log_func()

    def __init__(self, driver, locator, timeout: int = DEFAULT_TIMEOUT, description: str = None):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.description = description

    def click(self):
        self.log.info('Clicking on element')
        WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(self.locator)).click()

    def get_text(self):
        self.log.info('Getting element text')
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(self.locator)).text

