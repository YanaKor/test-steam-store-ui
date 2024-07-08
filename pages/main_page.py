import allure

from pages.base_page import BasePage
from data.test_data import Constants


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('')
    def check_main_page_title(self):
        page_title = Constants.MAIN_PAGE_TITLE.value
        assert self.driver.title == page_title,\
            f'Название страницы {self.driver.title}, а не {page_title}'
