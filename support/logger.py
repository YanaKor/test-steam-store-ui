import logging

logger = logging.getLogger(__name__)


def log_func():

    logger.setLevel(logging.INFO)
    # настройка обработчика и форматировщика
    handler = logging.FileHandler(f"{__name__}.log", mode='w')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    # добавление форматировщика к обработчику
    handler.setFormatter(formatter)
    # добавление обработчика к логгеру
    logger.addHandler(handler)
    return logger


log = log_func()
