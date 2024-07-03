import allure

from pages.base_page import BasePage
from locators import LoginPageLocators
from test_data import Constants


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Fill email field')
    def fill_email_field(self, email):
        self.click(LoginPageLocators.EMAIL_FIELD)
        self.fill_field(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Fill password field')
    def fill_password_field(self, password):
        self.click(LoginPageLocators.PASSWORD_FIELD)
        self.fill_field(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Click on submit button')
    def click_on_submit_button(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    @allure.step('checking that the login page opens')
    def check_login_page(self):
        page_title = Constants.LOGIN_PAGE_TITLE.value
        assert self.driver.title == page_title, \
            f'Название страницы {self.driver.title}, а не {page_title}'
        # assert self.find_element(MainPagesLocators.LOGIN_PAGE_TITLE).text == page_title

    @allure.step('Check loading element is displayed')
    def check_element_is_displayed(self):
        assert self.element_is_present(LoginPageLocators.LOADING_ELEMENT), 'Элемент не отображается на странице'

    @allure.step('Check error text is displayed')
    def check_error(self):
        error_message = Constants.ERROR_MESSAGE.value
        actual_message = self.get_text(LoginPageLocators.ERROR_MESSAGE)
        assert actual_message == error_message, \
            f'Ожидали {error_message}, получили ничего'
