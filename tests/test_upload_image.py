from support.logger import log
from pages.file_uploader_page import FileUploader
from test_data.urls import Urls
from test_data.data import ExpectedContent


def test_upload_image(browser):
    browser.get(Urls.UPLOAD_IMAGE)
    uploader_page = FileUploader(browser.get_original_driver())

    uploader_page.is_file_uploader_page_opened()
    uploader_page.upload_file()
    act_title = uploader_page.get_title_after_upload()
    assert act_title == ExpectedContent.UPLOADED_FILE_TITLE, \
        log.error(f'Expected title is {ExpectedContent.UPLOADED_FILE_TITLE}, but got {act_title}')
    assert uploader_page.get_file_name() == 'photo_2024.jpg', \
        log.error(f'Expected file name is photo_2024.jpg, but got {uploader_page.get_file_name()}')


def test_upload_image_with_dialogue_window(browser):
    browser.get(Urls.UPLOAD_IMAGE)
    uploader_page = FileUploader(browser.get_original_driver())
    uploader_page.is_file_uploader_page_opened()

    uploader_page.upload_file_via_field()
