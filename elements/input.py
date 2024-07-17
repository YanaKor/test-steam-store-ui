from elements.base_elements import BaseElement
from support.logger import log_func
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Input(BaseElement):
    log = log_func()

    def send_keys(self, text):
        self.log.info('')
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(self.locator)).send_keys(text)
