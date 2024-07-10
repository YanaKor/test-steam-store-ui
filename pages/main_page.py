import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.test_data import Constants

MAIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Welcome to Steam']")
UNIC_ELEMENT = (By.XPATH, "//a[contains(@class,'pulldown') and text()= 'Your Store']")


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_main_page_opened(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(UNIC_ELEMENT))
        except TimeoutError:
            return False
        return True
