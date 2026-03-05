import logging
import os
from datetime import datetime

log_dir="reports/logs"
os.makedirs(log_dir, exist_ok=True)
log_file =os.path.join(log_dir, f"automation_{datetime.now().date()}_{datetime.now().strftime('%H%M%S')}.log")

def get_logger(name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    
    # logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    
    file_Handler = logging.FileHandler(log_file, mode="a")
    file_Handler.setLevel(logging.INFO)
    file_Handler.setFormatter(formatter)

    console_Handler = logging.StreamHandler()
    console_Handler.setLevel(logging.INFO)
    console_Handler.setFormatter(formatter)

    logger.addHandler(file_Handler)
    logger.addHandler(console_Handler)

    return logger

