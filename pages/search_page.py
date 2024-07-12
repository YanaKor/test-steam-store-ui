import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from config.config import Config
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_FIELD = (By.XPATH, "//input[@id='store_nav_search_term']")
    SEARCH_BUTTON = (By.XPATH, "//a[@id='store_search_link']/img")
    SEARCH_ICON = (By.XPATH, "//div[@id='searchtag_tmpl' and contains(@style,  'inline-block')]")
    SORT_DROPDOWN = (By.XPATH, "//a[@id='sort_by_trigger']")
    SORT_BY_DESC = (By.XPATH, "//div[@class='dropcontainer']//a[@id='Price_DESC']")
    LOAD_LIST_BY_DESC = (By.XPATH, "//div[@id='search_result_container' and @style='opacity: 0.5;']")
    LIST_OF_GAMES = (By.XPATH, "//div[@id='search_resultsRows']//div[contains(@class, 'discount_final_price')]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Enter game name')
    def search_game(self, game):
        WebDriverWait(self.driver, timeout=Config.get_config_value('timeout')).until(
            ec.visibility_of_element_located(self.SEARCH_FIELD)).send_keys(game)
        WebDriverWait(self.driver, timeout=Config.get_config_value('timeout')).until(
            ec.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def is_search_results_page_opened(self):
        try:
            WebDriverWait(self.driver, timeout=Config.get_config_value('timeout')).until(
                ec.presence_of_element_located(self.SEARCH_ICON))
        except TimeoutError:
            return False
        return True

    @allure.step('Sort games by descending price')
    def sort_games_by_desc(self):
        WebDriverWait(self.driver, timeout=Config.get_config_value('timeout')).until(
            ec.element_to_be_clickable(self.SORT_DROPDOWN)).click()
        WebDriverWait(self.driver, timeout=Config.get_config_value('timeout')).until(
            ec.element_to_be_clickable(self.SORT_BY_DESC)).click()

    def get_list_of_games(self, quantity):
        WebDriverWait(self.driver, timeout=Config.get_config_value('timeout')).until_not(
            ec.visibility_of_element_located(self.LOAD_LIST_BY_DESC))
        elements = WebDriverWait(self.driver, timeout=Config.get_config_value('timeout')).until(
            ec.presence_of_all_elements_located(self.LIST_OF_GAMES))
        game_prices = []
        for element in elements[:quantity]:
            price = element.text
            game_prices.append(price)
        return game_prices
