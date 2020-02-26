import logging


def setup_logger():
    """Setup standard logger."""
    logger = logging.getLogger()
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    logging.basicConfig(level=logging.INFO)
    return logger
