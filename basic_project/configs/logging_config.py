# configs/logging_config.py
import os
import time
from datetime import date

today = date.today()

BASE_PATH = os.path.dirname(__file__)
LOGGER_FOLDER = f"{BASE_PATH}/../logger/log"
os.makedirs(LOGGER_FOLDER, exist_ok=True)
LOGGER_FILE = f"{LOGGER_FOLDER}/logger_{today}.txt"
