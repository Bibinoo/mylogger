import sys
import logging.config # to configure mylogger

PACKAGE_PATH = "C:\\Users\\denny_000\\Documents\\GitHub\\outlook"
sys.path.append(PACKAGE_PATH)
import logger.logger # path of the logger module

LOGGER_CONF_FILE = "conf/log_conf.yaml"

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
    logger.logger.setup_logging(PACKAGE_PATH, LOGGER_CONF_FILE)
    mylogger = logging.getLogger(__name__)
    main()
