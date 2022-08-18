import logging

# Default - only warning-critical is printed!
# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# Set the print level to logging.DEBUG - must be at the beginnning of the program
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d%Y %H: %M: %S')

# With new settings
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# Create your own logger for each module - good to understand where it comes from
logger = logging.getLogger(__name__)  # Create a logger with the name of the module - __main__

# Prints a warning with a path of main
logger.warning("Logger working")

# Create a handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Set level and format of the file log
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

# GENERATE DATA THAT'S IN THE file.log file!
logger.warning('This is a warning in line 42! (logged)')
logger.error('This is an error in line 43! (logged)')


