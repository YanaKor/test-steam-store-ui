import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

SEARCH_FIELD = (By.XPATH, "//input[@id='store_nav_search_term']")
SEARCH_BUTTON = ("xpath", "//a[@id='store_search_link']/img")
SEARCH_ICON = (By.XPATH, "//div[@id='searchtag_tmpl' and contains(@style,  'inline-block')]")
SORT_DROPDOWN = ('xpath', "//a[@id='sort_by_trigger']")
SORT_BY_DESC = ("xpath", "//div[@class='dropcontainer']//a[@id='Price_DESC']")
LOAD_LIST_BY_DESC = (By.XPATH, "//div[@id='search_result_container' and @style='opacity: 0.5;']")
LIST_OF_GAMES = (By.XPATH, "//div[@id='search_resultsRows']//div[contains(@class, 'discount_final_price')]")


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Enter game name')
    def search_game(self, game):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(SEARCH_FIELD)).send_keys(game)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(SEARCH_BUTTON)).click()

    def is_search_results_page_opened(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(SEARCH_ICON))
        except TimeoutError:
            return False
        return True

    @allure.step('Sort games by descending price')
    def sort_games_by_desc(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(SORT_DROPDOWN)).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(SORT_BY_DESC)).click()

    def get_list_of_games(self, quantity):
        WebDriverWait(self.driver, 10).until_not(ec.visibility_of_element_located(LOAD_LIST_BY_DESC))
        elements = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(LIST_OF_GAMES))
        game_prices = []
        for element in elements[:quantity]:
            price = element.text
            game_prices.append(price)
        return game_prices


