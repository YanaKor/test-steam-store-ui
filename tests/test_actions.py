from support.logger import log
from pages.horizontal_slider_page import HorizontalSliderPage
from test_data.urls import Urls
from test_data.data import ExpectedContent, random_text


def test_horizontal_slider(browser):
    browser.get(Urls.HORIZONTAL_SLIDER)
    slider_page = HorizontalSliderPage(browser.get_original_driver())
    slider_page.is_slider_page_open()
    slider_page.moves_right_arrow(5)
    value = float(slider_page.get_moves_value())
    assert value == 2.5, \
        log.error(f'Expected to be 2.5, got {value}')

