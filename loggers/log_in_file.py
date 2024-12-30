import logging
from datetime import datetime
from logging import DEBUG


def setup_logger():
    """Функция, которая будет логировать информационные сообщения, предупреждения и ошибки в файле логов.
    Функция должна использовать стандартную библиотеку logging. Файл логов должен создаваться каждый день с именем
     в формате "YYYY-MM-DD.log"."""

    logfile_name = datetime.now().strftime('%Y-%m-%d')

    # Логгер
    logger = logging.getLogger('daily_logger')
    logger.setLevel(DEBUG)
    # Хэндлер
    handler = logging.FileHandler(logfile_name)
    handler.setLevel(logging.DEBUG)
    # Форматтер
    formatter = logging.Formatter('%(asctime)s - %(level)s - %(message)s')

    # Добавляем форматтер к хэндлеру
    handler.setFormatter(formatter)

    # Добавляем хэндлер к логгеру
    logger.addHandler(handler)

    return logger


def log_messages(level, message):
    logger = setup_logger()

    if level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.debug(message)


setup_logger()
