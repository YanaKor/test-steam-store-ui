import pytest

from browser.browser import Browser
from config_utils.config_utils import ConfigUtils


@pytest.fixture(scope='function')
def browser():
    browser = Browser('chrome')
    browser.get(ConfigUtils.get_config_value('BASE_URL'))
    yield browser
    browser.quit()

    