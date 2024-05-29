# logger/logger.py
import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "..\\..\\"))
from logger.log_formatter import TimezoneFormatter
from configs import config, logging_config


import logging


# Configure logging
logging.basicConfig(
    filename=logging_config.LOGGER_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Update the root logger to use the timezone-aware formatter
logger = logging.getLogger()
for handler in logger.handlers:
    handler.setFormatter(
        TimezoneFormatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            timezone=config.TIMEZONE,
        )
    )


class Logger:
    def __init__(self):
        pass

    def log_info(self, msg):
        logging.info(msg)

    def log_error(self, msg, err):
        logging.error(f"{msg}: %s", err)
