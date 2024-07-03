from selenium.webdriver.common.by import By


class Urls:
    BASE_URL = 'https://store.steampowered.com'


class MainPagesLocators:
    MAIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Добро пожаловать в Steam']")
    LOGIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Войти']")
    LOGIN_BUTTON = (By.XPATH, ".//a[@class='global_action_link']")


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text' and @class='_2eKVn6g5Yysx9JmutQe7WV']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @class='_2eKVn6g5Yysx9JmutQe7WV']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[@type='submit' and text()='Войти']")
    LOADING_ELEMENT = (By.XPATH, ".//button[@class='_2QgFEj17t677s3x299PNJQ i9MK3T4AOf_2w3XTQ-Qpt']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='_1Mcy9wnDnt1Q72FijsNtHC']")
