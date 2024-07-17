from support.logger import log_func
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    log = log_func()

    def __init__(self, unique_element, driver, name):
        self.unique_element = unique_element
        self.driver = driver
        self.name = name

    def wait_for_opening(self, timeout=10):
        try:
            self.log.info(f"{self.name} page is opening")
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(self.unique_element))
        except Exception as e:
            self.log.error(f"Error waiting for {self.name} page to open: {e}")
            raise e

