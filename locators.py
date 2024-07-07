from selenium.webdriver.common.by import By


class Urls:
    BASE_URL = 'https://store.steampowered.com'


class MainPagesLocators:
    MAIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Добро пожаловать в Steam']")


#     LOGIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Войти']")
#     LOGIN_BUTTON = (By.XPATH, ".//a[@class='global_action_link']")
#
#
# class LoginPageLocators:
#     EMAIL_FIELD = (By.XPATH, ".//input[@type='text' and @class='_2eKVn6g5Yysx9JmutQe7WV']")
#     PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @class='_2eKVn6g5Yysx9JmutQe7WV']")
#     SUBMIT_BUTTON = (By.XPATH, ".//button[@type='submit' and text()='Войти']")
#     LOADING_ELEMENT = (By.XPATH, ".//button[@class='_2QgFEj17t677s3x299PNJQ i9MK3T4AOf_2w3XTQ-Qpt']")
#     ERROR_MESSAGE = (By.XPATH, "//div[@class='_1Mcy9wnDnt1Q72FijsNtHC']")


class SearchGamesLocators:
    # SEARCH_FIELD = (By.XPATH, "//input[@id='store_nav_search_term' and contains(@placeholder, 'поиск')]")
    SEARCH_FIELD = (By.XPATH, "//input[@id='store_nav_search_term']")
    SEARCH_BUTTON = ("xpath", "//a[@id='store_search_link']/img")
    SORT_DROPDOWN = ('xpath', "//a[@id='sort_by_trigger']")
    SORT_BY_DESC = ("xpath", "//div[@class='dropcontainer']//a[@id='Price_DESC']")
    LIST_OF_GAMES = (By.XPATH, "//div[@id='search_resultsRows']//span[@class='title']")
