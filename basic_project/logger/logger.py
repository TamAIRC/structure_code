import os
import sys
import logging

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../../"))
from logger.log_formatter import TimezoneFormatter
from configs import config, logging_config


class LoggerMeta(type):
    _instances = {}

    def __call__(cls, name="MongoDBLogger", *args, **kwargs):
        if name not in cls._instances:
            cls._instances[name] = super().__call__(name, *args, **kwargs)
        return cls._instances[name]


class Logger(metaclass=LoggerMeta):
    def __init__(self, name="MongoDBLogger"):
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

        self.logger = logging.getLogger(name)

    def log_info(self, msg, *args, **kwargs):
        """Log an informational message."""
        self.logger.info(msg, *args, **kwargs)

    def log_error(self, msg, err, *args, **kwargs):
        """
        Log an error message.

        Args:
            msg (str): The error message.
            err (Exception): Optional. The exception object associated with the error.
        """
        if err:
            self.logger.error(f"{msg}: {err}", *args, **kwargs)
        else:
            self.logger.error(msg, *args, **kwargs)
