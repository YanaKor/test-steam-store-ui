import logging


# def log_func():
#     logger = logging.basicConfig(level=logging.INFO, filename='logfile.log',
#                         format="%(asctime)s - %(levelname)s - %(message)s")
#     return logger

def log_func():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # настройка обработчика и форматировщика
    handler = logging.FileHandler(f"{__name__}.log", mode='w')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    # добавление форматировщика к обработчику
    handler.setFormatter(formatter)
    # добавление обработчика к логгеру
    logger.addHandler(handler)
    return logger
