import sys
import logging.config # to configure mylogger
import lib.logger # path of the logger module

# sys.path.append("C:\\Users\\denny_000\\Documents\\GitHub\\outlook")
PACKAGE_PATH = sys.path[0] # Retrieve the path of the current module
LOGGER_CONF_FILE = "conf/log_conf.yaml"

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
    lib.logger.setup_logging(PACKAGE_PATH, LOGGER_CONF_FILE)
    mylogger = logging.getLogger(__name__)
    main()
