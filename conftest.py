import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from patterns.singleton import Browser

from config.config import Config


# @pytest.fixture(scope="function", params=['en-US', 'ru'])
# def browser(request):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--window-size=1920,1080')
#     chrome_options.add_argument(f"--lang={request.param}")
#
#     browser = Browser(service=Service(), options=chrome_options)
#     browser.get(Config().get_config_value('BASE_URL'))
#     yield browser
#     (browser.quit()

@pytest.fixture(scope="function", params=Config.get_config_value('chrome_options'))
def browser():
    chrome_options = webdriver.ChromeOptions()
    for option in Config.get_config_value('chrome_options'):
        chrome_options.add_argument(option)
    browser = webdriver.Chrome(service=Service(), options=chrome_options)
    browser.get(Config().get_config_value('BASE_URL'))
    yield browser
    browser.quit()
