import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def find_element(self, locator):
        self.driver.find_elements(*locator)

    @allure.step('Clicking on element')
    def click(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator)).click()

    @allure.step('Fill text')
    def fill_field(self, locator, text):
        self.wait.until(ec.visibility_of_element_located(locator)).send_keys(text)

    def element_is_present(self, locator):
        self.wait.until(ec.presence_of_element_located(locator))

    @allure.step('Get text')
    def get_text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text
