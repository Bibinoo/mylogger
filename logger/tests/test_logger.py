import sys
import logging.config # to configure mylogger

# Setting up the global variables by importing the config.py module then -------
# importing the logger module --------------------------------------------------

from config import LOGGER # importing config.py as a conf module
LOGGER_PATH_FOLDER = LOGGER.PATH_FOLDER # setting the global variable
LOGGER_CONF_FILE = LOGGER.CONF_FILE # setting the global variable
LOGGER_LOGGING_LEVEL = LOGGER.LOGGING_LEVEL # setting the global variable

sys.path.append(LOGGER_PATH_FOLDER)
import logger # path of the logger module after appending the path

# ------------------------------------------------------------------------------

def test_something():
    mylogger.info('Testing something')
    mylogger.debug('Testing something in debug mode')
    mylogger.warning('Testing in warning mode')
    mylogger.critical('Testing something in critical mode')

def main():
    mylogger.info('Started')
    mylogger.debug('Started in debug mode')
    mylogger.warning('Started in warning mode')
    test_something()
    mylogger.info('Finished')

if __name__ == '__main__':
    logger.setup_logging(LOGGER_PATH_FOLDER, LOGGER_CONF_FILE,
        LOGGER_LOGGING_LEVEL)
    mylogger = logging.getLogger(__name__)
    main()
    logger.setup_logging(LOGGER_PATH_FOLDER, LOGGER_CONF_FILE,
        "logging.INFO")
    mylogger = logging.getLogger(__name__)
    main()
