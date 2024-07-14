import time

import allure
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from price_helpers import is_sorted_descending
from config.configutils import ConfigUtils


@allure.suite('test search')
class TestSearch:

    @pytest.mark.parametrize('game, quantity_of_games', [
        (ConfigUtils.get_test_data_value('The Witcher', 'name'),
         ConfigUtils.get_test_data_value('The Witcher', 'quantity_of_games')),
        (ConfigUtils.get_test_data_value('Fallout', 'name'),
         ConfigUtils.get_test_data_value('Fallout', 'quantity_of_games'))])
    def test_search_games(self, browser, game, quantity_of_games):
        browser, language = browser
        main_page = MainPage(browser)

        assert main_page.is_main_page_opened(language), 'The main page does not open'

        search_page = SearchPage(browser)
        search_page.search_game(game)
        assert search_page.is_search_results_page_opened(), 'The search results page did not open'
        search_page.sort_games_by_desc()
        sorted_list = search_page.get_list_of_games(quantity_of_games)
        assert is_sorted_descending(sorted_list), 'The list is not sorted in descending order'
