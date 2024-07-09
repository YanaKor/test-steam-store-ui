import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from single import SingletonChrome


from locators import Urls


# def pytest_addoption(parser):
#     parser.addoption(
#         '--language',
#         action='store',
#         default='en',
#         help='Language'
#     )


@pytest.fixture(params=['en-US', 'ru'])
def driver(request):
    # language = request.config.getoption('language')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    chrome_options.add_argument(f"--lang={request.param}")
    # chrome_options.add_argument("--lang=ru")
    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")
# def driver():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--window-size=1920,1080')
#
#     driver = SingletonChrome(service=Service(), options=chrome_options)
#     driver.get(Urls.BASE_URL)
#     yield driver
#     driver.quit()
