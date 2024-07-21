from support.logger import log
from pages.alerts_page import AlertPage
from test_data.urls import Urls
from test_data.data import ExpectedContent, random_text


def test_alerts(browser):
    browser.get(Urls.ALERTS)
    alert_page = AlertPage(browser.get_original_driver())

    # JS Alert
    alert_page.is_alerts_page_opened()
    alert_page.open_js_alert()
    assert browser.get_alert_text() == ExpectedContent.EXPECTED_JS_ALERT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.EXPECTED_JS_ALERT_TEXT},'
                  f' but got {browser.get_alert_text()}'))
    browser.switch_to_alert()
    browser.accept_alert()
    js_alert_act_result_text = alert_page.get_result_text()
    assert js_alert_act_result_text == ExpectedContent.JS_ALERT_EXP_RESULT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.JS_ALERT_EXP_RESULT_TEXT},'
                  f' but got {js_alert_act_result_text}'))

    # JS Confirm
    alert_page.open_js_confirm()
    assert browser.get_alert_text() == ExpectedContent.EXPECTED_JS_CONFIRM_TEXT, (
        log.error(f'Expected text is {ExpectedContent.EXPECTED_JS_CONFIRM_TEXT},'
                  f' but got {browser.get_alert_text()}'))
    browser.switch_to_alert()
    browser.accept_alert()
    js_confirm_act_result_text = alert_page.get_result_text()
    assert js_confirm_act_result_text == ExpectedContent.JS_CONFIRM_EXP_RESULT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.JS_CONFIRM_EXP_RESULT_TEXT},'
                  f' but got {js_confirm_act_result_text}'))

    # JS prompt
    alert_page.open_js_prompt()
    assert browser.get_alert_text() == ExpectedContent.EXPECTED_JS_PROMPT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.EXPECTED_JS_PROMPT_TEXT},'
                  f' but got {browser.get_alert_text()}'))
    browser.switch_to_alert()
    browser.send_keys_to_alert(random_text)
    browser.accept_alert()
    js_prompt_act_result_text = alert_page.get_result_text()
    assert js_prompt_act_result_text == ExpectedContent.JS_PROMPT_EXP_RESULT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.JS_PROMPT_EXP_RESULT_TEXT},'
                  f' but got {js_prompt_act_result_text}'))


def test_alerts_with_js_methods(browser):
    browser.get(Urls.ALERTS)
    alert_page = AlertPage(browser.get_original_driver())
    alert_page.is_alerts_page_opened()

    # JS Alert
    browser.execute_script("jsAlert()")
    browser.switch_to_alert()
    assert browser.get_alert_text() == ExpectedContent.EXPECTED_JS_ALERT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.EXPECTED_JS_ALERT_TEXT},'
                  f' but got {browser.get_alert_text()}'))
    browser.accept_alert()
    js_alert_act_result_text = alert_page.get_result_text()
    assert js_alert_act_result_text == ExpectedContent.JS_ALERT_EXP_RESULT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.JS_ALERT_EXP_RESULT_TEXT},'
                  f' but got {js_alert_act_result_text}'))

    # JS Confirm
    browser.execute_script('jsConfirm()')
    assert browser.get_alert_text() == ExpectedContent.EXPECTED_JS_CONFIRM_TEXT, (
        log.error(f'Expected text is {ExpectedContent.EXPECTED_JS_CONFIRM_TEXT},'
                  f' but got {browser.get_alert_text()}'))
    browser.switch_to_alert()
    browser.accept_alert()
    js_confirm_act_result_text = alert_page.get_result_text()
    assert js_confirm_act_result_text == ExpectedContent.JS_CONFIRM_EXP_RESULT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.JS_CONFIRM_EXP_RESULT_TEXT},'
                  f' but got {js_confirm_act_result_text}'))

    # JS prompt
    browser.execute_script('jsPrompt()')
    assert browser.get_alert_text() == ExpectedContent.EXPECTED_JS_PROMPT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.EXPECTED_JS_PROMPT_TEXT},'
                  f' but got {browser.get_alert_text()}'))
    browser.switch_to_alert()
    browser.send_keys_to_alert(random_text)
    browser.accept_alert()
    js_prompt_act_result_text = alert_page.get_result_text()
    assert js_prompt_act_result_text == ExpectedContent.JS_PROMPT_EXP_RESULT_TEXT, (
        log.error(f'Expected text is {ExpectedContent.JS_PROMPT_EXP_RESULT_TEXT},'
                  f' but got {js_prompt_act_result_text}'))
