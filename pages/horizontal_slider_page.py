from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.web_element import WebElement
from support.logger import log


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']//h3[text()='Horizontal Slider']")

    SLIDER_CONTAINER = (By.XPATH, "//div[@class='sliderContainer']//input[@type='range']")
    SLIDER_VALUE = (By.XPATH, "//div[@class='sliderContainer']//span[@id='range']")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='Horizontal Slider -> Title')
        self.page_name = 'Horizontal Slider'

        self.slider_container = WebElement(driver=self.driver, locator=self.SLIDER_CONTAINER,
                                           description='Horizontal Slider -> Slider Container')
        self.slider_value = WebElement(driver=self.driver, locator=self.SLIDER_VALUE,
                                       description='Horizontal Slider -> Slider Value')

    def is_slider_page_open(self):
        log.info(f'{self.page_name} is opening')
        self.wait_for_opening()

    def moves_right_arrow(self, num_of_moves):
        log.info(f'Move slides right for {num_of_moves} moves')
        self.slider_container.move_arrow(num_of_moves)

    def get_moves_value(self):
        log.info('Getting slider value')
        return self.slider_value.get_text()

