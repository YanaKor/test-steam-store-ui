import time

from support.logger import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, locator, timeout: int = DEFAULT_TIMEOUT, description: str = None):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.description = description

    def wait_for_presence(self):
        log.info('Waiting for presence of element')
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(self.locator))

    def wait_for_all_elements_presence(self):
        log.info('Waiting for presence list of elements')
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(self.locator))

    def wait_for_visibility_all_elements(self):
        log.info('Waiting for visibility list of elements on page')
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_all_elements_located(self.locator))

    def click(self):
        log.info('Clicking on element')
        WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(self.locator)).click()

    def right_click(self):
        locator = self.wait_for_presence()
        log.info('Right click on element')
        ActionChains(self.driver).move_to_element(locator).context_click().perform()

    def get_text(self):
        log.info(f'Getting element {self.locator} text')
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(self.locator)).text

    def move_arrow(self, num_of_moves):
        element = self.wait_for_presence()

        for i in range(num_of_moves):
            log.info('Move arrow for %d moves')
            element.send_keys(Keys.ARROW_RIGHT)

    def hover_on_element(self, elem):
        ActionChains(self.driver).move_to_element(elem).perform()
