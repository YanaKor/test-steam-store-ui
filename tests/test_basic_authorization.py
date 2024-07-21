from support.logger import log
from pages.authorization_page import AuthorizationPage
from test_data.data import ExpectedContent


def test_basic_auth(browser):
    auth_page = AuthorizationPage(browser.get_original_driver())
    auth_page.fill_authorization_form()
    auth_page.is_page_opened()
    actual_text = auth_page.get_actual_text_from_base_auth_page()
    assert actual_text == ExpectedContent.EXPECTED_TEXT_BASE_AUTH, \
        log.error(f'Expected text is {ExpectedContent.EXPECTED_TEXT_BASE_AUTH},'
                  f' but got {actual_text}')
