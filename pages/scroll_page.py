from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.web_element import WebElement


class ScrollPage(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']//h3[text()='Infinite Scroll']")
    PARAGRAPH = (By.XPATH, "//div[@class='jscroll-added']")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='Infinite Scroll -> Title')
        self.paragraph = WebElement(driver=self.driver, locator=self.PARAGRAPH,
                                    description='Infinite Scroll -> Paragraph on page')

    def is_scroll_page_opened(self):
        self.wait_for_opening()

    def get_all_paragraphs_on_page(self):
        return self.paragraph.wait_for_visibility_all_elements()
