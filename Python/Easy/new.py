# main_script.py
from log import SingletonLogger

# Get the logger instance
logger = SingletonLogger()

# Now you can use the logger in your file
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')