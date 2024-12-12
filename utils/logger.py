"""
Created on 12-Dec-2024

@author: Smart Travel Consultant Team
"""

import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    """
    Sets up the logging configuration for the Smart Travel Consultant project.
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create logs directory if it doesn't exist
    log_dir = os.getenv("SMART_TRAVEL_LOG_DIR", "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Define log file path
    log_file_path = os.path.join(log_dir, "smart_travel_consultant.log")

    # Set up rotating file handler
    handler = RotatingFileHandler(log_file_path, maxBytes=5_000_000, backupCount=5, encoding='utf-8')

    # Define logging format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Create logger
    logger = logging.getLogger("SmartTravelLogger")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    # Optional: Add a stream handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Logger is configured and ready to use.")
    logger.error("This is a test error message.")
