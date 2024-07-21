import os

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.input import Input
from elements.button import Button


class FileUploader(BasePage):
    UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//div[@class='example']//h3[text()='File Uploader']")
    UPLOAD_INPUT = (By.ID, 'file-upload')
    UPLOAD_BUTTON = (By.ID, "file-submit")
    RESULT_OF_UPLOAD_TITLE = (By.XPATH, "//div[@class='example']//h3[text()='File Uploaded!']")
    UPLOADED_FILE_NAME = (By.ID, "uploaded-files")
    DRAG_AND_DROP_UPLOAD = (By.ID, "drag-drop-upload")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = WebElement(driver=self.driver, locator=self.UNIQUE_ELEMENT_LOCATOR,
                                         description='File Uploader -> Title')
        self.page_name = 'File Uploader'

        self.upload_input = Input(driver=self.driver, locator=self.UPLOAD_INPUT,
                                  description='File Uploader -> Upload field')

        self.upload_button = Button(driver=self.driver, locator=self.UPLOAD_BUTTON,
                                    description='File Uploader -> Submit Upload Button')

        self.uploaded_title = WebElement(driver=self.driver, locator=self.RESULT_OF_UPLOAD_TITLE,
                                         description='File Uploader -> Page title after upload')

        self.uploaded_file = WebElement(driver=self.driver, locator=self.UPLOADED_FILE_NAME,
                                        description='File Uploader -> File name after upload')
        self.upload_field = Input(driver=self.driver, locator=self.DRAG_AND_DROP_UPLOAD,
                                       description='File Uploader -> Drag and Drop field')

        self.file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                      'test_data', 'photo_2024.jpg')

    def is_file_uploader_page_opened(self):
        self.wait_for_opening()

    def upload_file(self):
        self.upload_input.send_keys(self.file_path)
        self.upload_button.click()

    def get_title_after_upload(self):
        return self.uploaded_title.get_text()

    def get_file_name(self):
        return self.uploaded_file.get_text()

    def upload_file_via_field(self):
        self.upload_field.click()
        self.upload_field.send_keys(self.file_path)
