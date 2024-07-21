from selenium.webdriver.common.by import By
from elements.web_element import WebElement

from support.logger import log
from pages.base_page import BasePage


class AuthorizationPage(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']/h3[text()='Basic Auth']")
    CONTENT_TEXT = (By.XPATH, "//div[@class='example']/p[contains(text(), 'Congratulations!')]")
    USER_NAME = 'admin'
    PASSWORD = 'admin'

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='Authorization page -> Title')
        self.page_name = 'Base Authorization Page'

        self.content_text = WebElement(self.driver, self.CONTENT_TEXT, description='Authorization page -> Content text')

    def fill_authorization_form(self):
        self.driver.get(f'https://{self.USER_NAME}:{self.PASSWORD}@the-internet.herokuapp.com/basic_auth')

    def is_page_opened(self):
        log.info(f'{self.page_name} is opening')
        self.wait_for_opening()

    def get_actual_text_from_base_auth_page(self):
        log.info('Checking text after authorization')
        return self.content_text.get_text()

