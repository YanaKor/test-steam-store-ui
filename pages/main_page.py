import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config.configutils import ConfigUtils


class MainPage(BasePage):
    # MAIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Welcome to Steam']")
    UNIC_ELEMENT = (By.XPATH, "//a[contains(@class,'pulldown') and text()= 'Your Store']")
    UNIC_ELEMENT_RU = (By.XPATH, "//a[contains(@class,'pulldown') and text()= 'Магазин']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_main_page_opened(self, language):
        try:
            if language == 'en-US':
                WebDriverWait(self.driver, timeout=ConfigUtils.get_config_value('timeout')).until(
                    ec.presence_of_element_located(self.UNIC_ELEMENT))
            else:
                WebDriverWait(self.driver, timeout=ConfigUtils.get_config_value('timeout')).until(
                    ec.presence_of_element_located(self.UNIC_ELEMENT_RU))

        except TimeoutError:
            return False
        return True
