# config.py
import os
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logging(filename="app_log"):
    """
    Sets up basicConfig logging for this project so that that other files don't
    have to set it up each time.

    filename = A string for the base filename for the log.  Defaults to "app_log"

    The LOGGING_LEVEL is setup in the .env file

    """

    # Default to "INFO" if not set.
    logging_level_str = os.getenv('LOGGING_LEVEL','INFO').upper() 
    # ensures that if an invalid level is provided, it defaults to logging.INFO
    logging_level = getattr(logging, logging_level_str, logging.INFO) 

    # Setup folders and file names
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_file_path = os.path.join(log_directory, f"{filename}.log")

    # Create a TimedRotatingFileHandler
    # creates a new log file every midnight and keeps the last 30 days of log files.
    file_handler = TimedRotatingFileHandler(log_file_path, when="midnight", interval=1, backupCount=30)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


    # Setup basic config
    logging.basicConfig(level = logging_level,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            # logging.FileHandler(log_file_path),
                            file_handler,
                            logging.StreamHandler()
                        ])
    logging.info('Log basicConfig() complete!')


