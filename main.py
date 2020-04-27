# ------------------------------------------------------------------------------
# Setting up mylogger package --------------------------------------------------
# ------------------------------------------------------------------------------

import sys
import os
import logging.config # Initial settup of python login to configure mylogger

# Setting up the global variables by importing the config.py module then -------
# importing the logger module --------------------------------------------------

from config import LOGGER # Initial settup of python login to configure mylogger
LOGGER_PATH_FOLDER = LOGGER.PATH_FOLDER # setting the logger package path as a global variable
LOGGER_CONF_FILE = LOGGER.CONF_FILE # setting the logger configuration file as a global variable
LOGGER_LOGGING_LEVEL = LOGGER.LOGGING_LEVEL # setting the default logging lever as a global variable

sys.path.append(LOGGER_PATH_FOLDER)
from loggerpkg import myloggerscript # import module myloggerscript (pythin script) from loggerpkg package (folder)

# Setting up mylogger functions ------------------------------------------------
import inspect

def displayLoggerSetupMsg():
    print("Importing the configuration file config.py from " + os.getcwd())
    print("Setting up the logger configuration file path as " + LOGGER_CONF_FILE)
    print("Setting up the default logging level as " + LOGGER_LOGGING_LEVEL)

# ------------------------------------------------------------------------------
# End of setting up mylogger package -------------------------------------------
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Setting up global functions --------------------------------------------------
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Setting up specific functions ------------------------------------------------
# ------------------------------------------------------------------------------

def do_something():
    mylogger.info('Doing something')
    mylogger.debug('Doing something in debug mode')
    mylogger.critical('Doing something in critical mode')

# ------------------------------------------------------------------------------
# Main -------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main():
	mylogger.info('Started')
	mylogger.debug('Started in debug mode')
	mylogger.warning('Started in warning mode')
	do_something()
	mylogger.info('Finished')
	mylogger.info('Started')
	mylogger.debug('Started in debug mode')
	mylogger.warning('Started in warning mode')
	do_something()
	mylogger.info('Finished')
    

if __name__ == '__main__':
    displayLoggerSetupMsg()
    myloggerscript.setup_logging(LOGGER_PATH_FOLDER, LOGGER_CONF_FILE,
        LOGGER_LOGGING_LEVEL)
    mylogger = logging.getLogger(__name__)
    main()
