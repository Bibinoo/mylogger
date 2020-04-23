import sys
import os
import logging.config # to configure mylogger

# Setting up the global variables by importing the config.py module then -------
# importing the logger module --------------------------------------------------

from config import LOGGER # importing config.py as a conf module
LOGGER_PATH_FOLDER = LOGGER.PATH_FOLDER # setting the global variable
LOGGER_CONF_FILE = LOGGER.CONF_FILE # setting the global variable
LOGGER_LOGGING_LEVEL = LOGGER.LOGGING_LEVEL # setting the global variable

sys.path.append(LOGGER_PATH_FOLDER)
from loggerpkg import myloggerscript # import module myloggerscript (pythin script) from loggerpkg package (folder)
# ------------------------------------------------------------------------------

def display_setup_msg():
    print("Importing the configuration file config.py from " + os.getcwd())
    print("Setting up the logger configuration file path as " + LOGGER_CONF_FILE)
    print("Setting up the default logging level as " + LOGGER_LOGGING_LEVEL)

def do_something():
    mylogger.info('Doing something')
    mylogger.debug('Doing something in debug mode')
    mylogger.critical('Doing something in critical mode')

def main():
    mylogger.info('Started')
    mylogger.debug('Started in debug mode')
    mylogger.warning('Started in warning mode')
    do_something()
    mylogger.info('Finished')

if __name__ == '__main__':
    display_setup_msg()
    myloggerscript.setup_logging(LOGGER_PATH_FOLDER, LOGGER_CONF_FILE,
        LOGGER_LOGGING_LEVEL)
    mylogger = logging.getLogger(__name__)
    main()
