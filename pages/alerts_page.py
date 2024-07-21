from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.button import Button
from elements.web_element import WebElement
from support.logger import log


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']//h3[text()='JavaScript Alerts']")

    JS_ALERT_BTN = (By.XPATH, "//button[@onclick='jsAlert()']")
    JS_CONFIRM_BTN = (By.XPATH, "//button[@onclick='jsConfirm()']")
    JS_PROMPT_BTN = (By.XPATH, "//button[@onclick='jsPrompt()']")
    ALERT_RESULT = (By.XPATH, "//p[@id='result' and contains(text(), 'You')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='JS Alerts -> Title')
        self.page_name = 'JavaScripts Alerts'

        self._js_alert = Button(self.driver, self.JS_ALERT_BTN, description='Click for JS Alert')
        self._js_confirm = Button(self.driver, self.JS_CONFIRM_BTN, description='Click for JS Confirm')
        self._js_prompt = Button(self.driver, self.JS_PROMPT_BTN, description='Click for JS Prompt')
        self.alert_result_text = WebElement(driver=self.driver, locator=self.ALERT_RESULT,
                                            description='JS Alerts -> Alert result text')

    def is_alerts_page_opened(self):
        log.info(f'{self.page_name} is opening')
        self.wait_for_opening()

    def open_js_alert(self):
        log.info('JS alert is opening')
        self._js_alert.click()

    def open_js_confirm(self):
        log.info('JS confirm is opening')
        self._js_confirm.click()

    def open_js_prompt(self):
        log.info('JS prompt is opening')
        self._js_prompt.click()

    def get_result_text(self):
        log.info('Getting result alert text')
        return self.alert_result_text.get_text()







