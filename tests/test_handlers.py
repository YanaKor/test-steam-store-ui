import time

from support.logger import log
from pages.handlers_page import HandlersPage
from test_data.urls import Urls


def test_handler(browser):
    browser.get(Urls.HANDLERS)
    handler_page = HandlersPage(browser.get_original_driver())

    handler_page.is_handler_page_open()
    handler_page.open_new_window()
    browser.switch_to_window(-1)
    assert handler_page.get_new_window_title() == 'New Window', (
        log.error(f"Expected page title is 'New Window', but got {handler_page.get_new_window_title()}"))
    assert browser.title() == 'New Window', \
        log.error(f"Expected browser title is 'New Window', but got {browser.title()}")
    time.sleep(3)

    browser.switch_to_window(0)
    time.sleep(3)
    assert handler_page.is_handler_page_open(), log.error(f"Handler page does not open")

    handler_page.open_new_window()
    assert handler_page.get_new_window_title() == 'New Window', (
        log.error(f"Expected page title is 'New Window', but got {handler_page.get_new_window_title()}"))
    assert browser.title() == 'New Window', \
        log.error(f"Expected browser title is 'New Window', but got {browser.title()}")
    time.sleep(3)

    browser.close_tab()

