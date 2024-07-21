from support.logger import log
from pages.context_menu_page import ContextMenuPage
from test_data.urls import Urls
from test_data.data import ExpectedContent


def test_context_menu(browser):
    browser.get(Urls.CONTEXT_MENU)
    context_page = ContextMenuPage(browser.get_original_driver())
    context_page.is_context_menu_page_opened()
    context_page.right_click_on_context_menu()

    browser.switch_to_alert()
    assert browser.get_alert_text() == ExpectedContent.EXP_CONTEXT_MENU_ALERT, \
        log.error(f'Expected text is {ExpectedContent.EXP_CONTEXT_MENU_ALERT},'
                  f' but got {browser.get_alert_text()}')
    browser.accept_alert()
