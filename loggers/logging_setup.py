import logging

logger = logging.getLogger("log message")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    handler = logging.FileHandler("log_file_name.txt")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
