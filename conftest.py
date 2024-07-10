import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from patterns.singleton import Browser

from config.config import Config


@pytest.fixture(scope="function", params=['en-US', 'ru'])
def browser(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument(f"--lang={request.param}")

    browser = Browser(service=Service(), options=chrome_options)
    browser.get(Config().load_config())
    yield browser
    browser.quit()
