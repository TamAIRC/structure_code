# logger/log_formatter.py
import logging
from datetime import datetime
import pytz


class TimezoneFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, timezone=None):
        super().__init__(fmt, datefmt)
        self.timezone = pytz.timezone(timezone)

    def formatTime(self, record, datefmt=None):
        record_time = datetime.fromtimestamp(record.created, self.timezone)
        if datefmt:
            return record_time.strftime(datefmt)
        else:
            return record_time.isoformat()
