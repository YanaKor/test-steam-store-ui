from support.logger import log
from pages.scroll_page import ScrollPage
from test_data.urls import Urls


def test_alerts(browser):
    browser.get(Urls.INFINITY_SCROLL)
    scroll_page = ScrollPage(browser.get_original_driver())

    scroll_page.is_scroll_page_opened()
    paragraph_count = 0
    while paragraph_count < 27:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        paragraphs = scroll_page.get_all_paragraphs_on_page()
        paragraph_count = len(paragraphs)

    if paragraph_count == 27:
        log.info('The number of paragraphs matches the age of the engineer')
    else:
        log.error('The number of paragraphs does not match the age of the engineer')
