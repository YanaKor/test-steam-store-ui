from enum import Enum

from faker import Faker

fake = Faker()


class Constants(Enum):
    MAIN_PAGE_TITLE = 'Добро пожаловать в Steam'
    LOGIN_PAGE_TITLE = 'Войти'
    ERROR_MESSAGE = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'


class TestDataGenerator:

    @staticmethod
    def generate_email():
        email = fake.email()
        return email

    @staticmethod
    def generate_password():
        password = fake.password(length=9, special_chars=True)
        return password
