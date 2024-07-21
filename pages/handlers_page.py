from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.web_element import WebElement


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']//h3[text()='Opening a new window']")
    NEW_WINDOW_LINK = (By.XPATH, "//div[@class='example']/a")
    NEW_WINDOW_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='Handlers -> Title')
        self.page_name = 'Handlers'
        self.new_window = WebElement(driver=self.driver, locator=self.NEW_WINDOW_LINK,
                                     description='Handlers -> Open a new window link')
        self.new_window_title = WebElement(driver=self.driver, locator=self.NEW_WINDOW_TITLE,
                                           description='New window title')

    def is_handler_page_open(self):
        self.wait_for_opening()

    def open_new_window(self):
        self.new_window.click()

    def get_new_window_title(self):
        return self.new_window_title.get_text()
