from support.logger import log
from pages.hovers_page import HoversPage
from test_data.urls import Urls
from test_data.data import ExpectedContent


def test_hovers(browser):
    browser.get(Urls.HOVERS)
    hovers_page = HoversPage(browser.get_original_driver())
    hovers_page.is_hovers_page_open()
    hovers_page.hover_on_avatar()

