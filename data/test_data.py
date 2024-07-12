from enum import Enum


class Constants(str, Enum):
    MAIN_PAGE_TITLE = 'Добро пожаловать в Steam'
    MAIN_PAGE_TITLE_EN = 'Welcome to Steam'


class TestData(int, Enum):
    THE_WITCHER = 10
    FALLOUT = 20
