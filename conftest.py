import pytest

from browser.browser import Browser
from test_data.urls import Urls


@pytest.fixture(scope='function')
def browser():
    browser = Browser('chrome')
    browser.get(Urls.BASE_URL)
    yield browser
    browser.quit()

    