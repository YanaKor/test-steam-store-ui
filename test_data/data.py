import random
import string

random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))


class ExpectedContent:
    EXPECTED_TEXT_BASE_AUTH = 'Congratulations! You must have the proper credentials.'

    EXPECTED_JS_ALERT_TEXT = 'I am a JS Alert'
    JS_ALERT_EXP_RESULT_TEXT = 'You successfully clicked an alert'

    EXPECTED_JS_CONFIRM_TEXT = 'I am a JS Confirm'
    JS_CONFIRM_EXP_RESULT_TEXT = 'You clicked: Ok'

    EXPECTED_JS_PROMPT_TEXT = 'I am a JS prompt'
    JS_PROMPT_EXP_RESULT_TEXT = f'You entered: {random_text}'

    EXP_CONTEXT_MENU_ALERT = 'You selected a context menu'

    UPLOADED_FILE_TITLE = 'File Uploaded!'


