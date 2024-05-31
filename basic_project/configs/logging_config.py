# configs/logging_config.py
import os 
BASE_PATH = os.path.dirname(__file__) 
LOGGING_FOLDER = os.path.join(BASE_PATH, '../logger/log')
os.makedirs(LOGGING_FOLDER, exist_ok=True)
LOGGER_FILE = os.path.join(LOGGING_FOLDER, 'logger.txt')
print("LOGGER_FILE: ", LOGGER_FILE)