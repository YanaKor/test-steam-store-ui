import time

import allure
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage


@allure.suite('test search')
class TestSearch:

    @pytest.mark.parametrize('game, quantity_of_games', [('The Witcher', 10), ('Fallout', 20)])
    def test_search_games(self, driver, game, quantity_of_games):
        main_page = MainPage(driver)
        main_page.check_main_page_title()
        time.sleep(5)

        search_page = SearchPage(driver)
        search_page.search_game(game)
        search_page.sort_games_by_desc()
        time.sleep(5)
        search_page.get_list_of_games(quantity_of_games)


