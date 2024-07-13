import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from patterns.singleton import Browser

from config.configutils import ConfigUtils


@pytest.fixture(scope="function", params=ConfigUtils.get_config_value('languages'))
def browser(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--lang={request.param}")
    for option in ConfigUtils.get_config_value('chrome_options'):
        chrome_options.add_argument(option)
    browser = Browser(service=Service(), options=chrome_options)
    browser.get(ConfigUtils().get_config_value('BASE_URL'))
    yield browser
    Browser.quit()
