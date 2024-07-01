import time

import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from test_data import TestDataGenerator


@allure.suite('test user login')
class TestLogin:
    def test_login(self, driver):
        main_page = MainPage(driver)
        main_page.check_main_page_title()
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.check_login_page()
        login_page.fill_email_field(TestDataGenerator.generate_email())
        login_page.fill_password_field(TestDataGenerator.generate_password())
        login_page.click_on_submit_button()
        # login_page.check_element_is_displayed()
        time.sleep(5)
        login_page.check_error()
