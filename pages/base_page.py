from support.logger import log


class BasePage:
    UNIQUE_ELEMENT_LOCATOR = None

    def __init__(self, driver):
        self.driver = driver
        self.unique_element = None
        self.page_name = None

    def wait_for_opening(self):
        try:
            log.info(f"{self.page_name} page is opening")
            self.unique_element.wait_for_presence()
        except TimeoutError as e:
            log.error(f"Error waiting for {self.page_name} page to open: {e}")
            return False
        return True
