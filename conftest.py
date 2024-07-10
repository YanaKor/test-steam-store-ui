import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from patterns.singleton import SingletonChrome

from config.config import Config


# @pytest.fixture(params=['en-US', 'ru'])
# def driver(request):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--window-size=1920,1080')
#     chrome_options.add_argument(f"--lang={request.param}")
#     driver = webdriver.Chrome(service=Service(), options=chrome_options)
#
#     driver.get(Urls.BASE_URL)
#     yield driver
#     driver.quit()


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--lang=en-US")

    driver = SingletonChrome(service=Service(), options=chrome_options)
    driver.get(Config().load_config())
    yield driver
    driver.quit()
