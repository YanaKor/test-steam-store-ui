from elements.base_elements import BaseElement
from support.logger import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Input(BaseElement):

    def send_keys(self, text):
        log.info('Sending text to input')
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(self.locator)).send_keys(text)


