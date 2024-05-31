# logger/logger.py
import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "..\\..\\"))
from configs import logging_config


import logging

# Configure logging
logging.basicConfig(
    filename= logging_config.LOGGER_FILE,
    level=logging.DEBUG,                
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S'      
)

class Logger: 
    def __init__(self): 
        pass

    def log_info(message): 
        logging.info(message)
    
    def log_error(msg, err):
        logging.error(f"{msg}: %s", err)