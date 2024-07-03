import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


from locators import Urls


@pytest.fixture()
def driver():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()
