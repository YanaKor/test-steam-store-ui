import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.web_element import WebElement
from support.logger import log


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']//h3[text()='Hovers']")

    USER_AVATAR = (By.XPATH, "//img[@alt='User Avatar']")
    USER_NAME = (By.XPATH, "//div[@class='figcaption']//h5")
    USER_LINK = (By.XPATH, "//a[contains (@href, 'users')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='Hovers -> Title')
        self.page_name = 'Hovers'

        self.user_avatar = WebElement(driver=self.driver, locator=self.USER_AVATAR,
                                      description='Hovers -> User Avatar')
        self.user_name = WebElement(driver=self.driver, locator=self.USER_NAME,
                                    description='Hovers -> User Name')
        self.user_link = WebElement(driver=self.driver, locator=self.USER_LINK,
                                    description='Hovers -> User Link')

    def is_hovers_page_open(self):
        log.info(f'{self.page_name} is opening')
        self.wait_for_opening()

    def hover_on_avatar(self):
        users = self.user_avatar.wait_for_all_elements_presence()
        for user in users:
            log.info('')
            self.user_avatar.hover_on_element(user)
            time.sleep(2)
            name = self.get_user_name()
            print(name)

    def get_user_name(self):
        return self.user_name.get_text()
