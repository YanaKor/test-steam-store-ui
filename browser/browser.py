from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser.browser_factory import BrowserFactory
from support.logger import log


class Browser:
    DEFAULT_TIMEOUT = 10

    def __init__(self, browser_name='chrome', timeout=DEFAULT_TIMEOUT):
        self.browser_factory = BrowserFactory(browser_name)
        self.driver = self.browser_factory.create_browser()
        self.timeout = timeout

    def get(self, url):
        log.info(f'Opening page {url}')
        self.driver.get(url)

    def get_original_driver(self):
        log.info('Getting original driver from selenium')
        return self.driver

    def get_current_url(self):
        log.info('Getting current url')
        return self.driver.get_current_url

    def back(self):
        log.info('Go back to pevious page')
        return self.driver.back()

    def switch_to_window(self, index):
        log.info('Switch to new window')
        return self.driver.switch_to.window(self.driver.window_handles[index])

    def title(self):
        log.info('Get window title')
        return self.driver.title

    def close_tab(self):
        log.info('Close tab')
        self.driver.close()

    def quit(self):
        log.info('Closing the browser')
        self.driver.quit()

    def wait_for_opening_alert(self):
        try:
            log.info(f"Alert is opening")
            WebDriverWait(self.driver, self.timeout).until(ec.alert_is_present())
        except Exception as e:
            log.error(f"Error waiting for alert to open: {e}")
            raise e

    def switch_to_alert(self):
        self.wait_for_opening_alert()
        log.info('Switching to alert')
        self.driver.switch_to.alert

    def accept_alert(self):
        log.info('Accept the alert')
        WebDriverWait(self.driver, self.timeout).until(ec.alert_is_present()).accept()

    def get_alert_text(self):
        log.info('Getting  alert text')
        return WebDriverWait(self.driver, self.timeout).until(ec.alert_is_present()).text

    def send_keys_to_alert(self, text):
        log.info('Sending keys to alert')
        WebDriverWait(self.driver, self.timeout).until(ec.alert_is_present()).send_keys(text)

    def execute_script(self, script):
        log.info('Execute js script')
        self.driver.execute_script(script)


