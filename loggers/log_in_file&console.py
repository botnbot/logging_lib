import logging
from datetime import datetime
from logging import getLogger, DEBUG, Formatter


def setup_logger():
    """Функция, которая будет логировать информационные сообщения, предупреждения и ошибки в файле логов и консоли.
    Функция должна использовать стандартную библиотеку logging. Файл логов должен создаваться каждый день с именем
     в формате "YYYY-MM-DD.log"."""

    logfile_name = datetime.now().strftime('%Y-%m-%d')

    logger = getLogger('prosto_logger')
    logger.setLevel(DEBUG)

    if not logger.handlers:

        file_handler = logging.FileHandler(logfile_name)
        file_handler.setLevel(DEBUG)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(DEBUG)

        formatter = Formatter("%(asctime)s - %(level)s - %(message)s")

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

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
