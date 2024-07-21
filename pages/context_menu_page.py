from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.web_element import WebElement
from support.logger import log


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']//h3[text()='Context Menu']")

    BOX_FOR_CLICK = (By.ID, "hot-spot")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='Context Menu -> Title')
        self.page_name = 'Context Menu'

        self.box = WebElement(driver=self.driver, locator=self.BOX_FOR_CLICK,
                              description='Context Menu -> Box for clicking')

    def is_context_menu_page_opened(self):
        log.info(f'{self.page_name} is opening')
        self.wait_for_opening()

    def right_click_on_context_menu(self):
        log.info('Right click on context menu')
        self.box.right_click()
