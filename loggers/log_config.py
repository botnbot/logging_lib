import logging
from logging import Formatter, getLogger

"""Создайте базовый конфигурационный файл логирования. Залогируйте несколько сообщений разных уровней (INFO,WARNING,
ERROR,DEBUG)."""
# Базовая конфигурация логирования
logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG, format="%(name)s - %(message)s")
# Залогируйте несколько сообщений разных уровней (INFO,WARNING,ERROR,DEBUG).
logger = getLogger("just_loger")
logger.debug("bug found")
logger.info("something_happens")
logger.warning("attention")
logger.error("error")
# Измените формат вывода логера, чтобы включить временную метку и уровень логирования.
filehandler = logging.FileHandler("log.txt")
formatter = Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
# Добавьте второй обработчик для вывода сообщений в консоль, помимо записи в файл.
consolehandler = logging.StreamHandler()
logger.addHandler(consolehandler)

"""Создайте два различных логера, каждый — записывающий сообщения в свой файл."""
# Создаем два различных логера(loger)
loger1 = getLogger("first_loger")
loger1.setLevel(logging.DEBUG)

loger2 = getLogger("second_loger")
loger2.setLevel(logging.INFO)

# Создаем два обработчика(handler) к этим логерам(loger), каждый пишет лог в свой лог-файл
filehandler1 = logging.FileHandler("first_log.txt")
filehandler1.setLevel(logging.WARNING)

filehandler2 = logging.FileHandler("second_log.txt")
filehandler2.setLevel(logging.ERROR)

# Присоединяем эти обработчики (handler), каждый к своему логеру(loger)
loger1.addHandler(filehandler1)
loger2.addHandler(filehandler2)
