import logging


def set_logger():
    logger = logging.getLogger("HTTP-client")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("HTTP-client.log")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s ' ' %(levelname)s ' '  %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


LOGGER = set_logger()