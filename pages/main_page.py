import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.test_data import Constants

MAIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Welcome to Steam']")


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('')
    def check_main_page_title(self):
        page_title = Constants.MAIN_PAGE_TITLE_EN.value
        assert self.driver.title == page_title, \
            f'Page title is {self.driver.title}, not {page_title}'
