import allure
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from price_helpers import is_sorted_descending
from data.test_data import TestData


@allure.suite('test search')
class TestSearch:

    @pytest.mark.parametrize('game, quantity_of_games', [(TestData.THE_WITCHER.name.replace('_', ' '),
                                                          TestData.THE_WITCHER.value),
                                                         (TestData.FALLOUT.name, TestData.FALLOUT.value)])
    def test_search_games(self, browser, game, quantity_of_games):
        main_page = MainPage(browser)
        assert main_page.is_main_page_opened(), 'The main page does not open'

        search_page = SearchPage(browser)
        search_page.search_game(game)
        assert search_page.is_search_results_page_opened(), 'The search results page did not open'
        search_page.sort_games_by_desc()
        sorted_list = search_page.get_list_of_games(quantity_of_games)
        assert is_sorted_descending(sorted_list), 'The list is not sorted in descending order'


