import time

import allure

from pages.base_page import BasePage
from locators import SearchGamesLocators


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Enter game name')
    def search_game(self, game):
        self.fill_field(SearchGamesLocators.SEARCH_FIELD, game)
        self.click(SearchGamesLocators.SEARCH_BUTTON)

    @allure.step('Sort games by descending price')
    def sort_games_by_desc(self):
        self.click(SearchGamesLocators.SORT_DROPDOWN)
        self.click(SearchGamesLocators.SORT_BY_DESC)

    def get_list_of_games(self, quantity):
        print('begin')
        elements = []
        elements = self.find_all_elements(SearchGamesLocators.LIST_OF_GAMES)
        print(elements)
        print('________')
        list_of_elements = elements[:quantity]
        print(list_of_elements)
        print('_______')
        for element in list_of_elements:
            elements.append(element)
            print(elements.text)
