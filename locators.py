from selenium.webdriver.common.by import By


class Urls:
    BASE_URL = 'https://store.steampowered.com'


class MainPagesLocators:
    MAIN_PAGE_TITLE = (By.XPATH, ".//title[text()='Добро пожаловать в Steam']")


class SearchGamesLocators:
    # SEARCH_FIELD = (By.XPATH, "//input[@id='store_nav_search_term' and contains(@placeholder, 'поиск')]")
    SEARCH_FIELD = (By.XPATH, "//input[@id='store_nav_search_term']")
    SEARCH_BUTTON = ("xpath", "//a[@id='store_search_link']/img")
    SORT_DROPDOWN = ('xpath', "//a[@id='sort_by_trigger']")
    SORT_BY_DESC = ("xpath", "//div[@class='dropcontainer']//a[@id='Price_DESC']")
    LIST_OF_GAMES = (By.XPATH, "//div[@id='search_resultsRows']//span[@class='title']")
