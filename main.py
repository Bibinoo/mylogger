import os
import sys
import logging.config
import yaml
import lib.logger

# sys.path.append("C:\\Users\\denny_000\\Documents\\GitHub\\outlook")
print(sys.path[0])

def do_something():
    logging.info('Doing something')
    logging.debug('Doing something in debug mode')
    logging.critical('Doing something in critical mode')

def main():
    logging.info('Started')
    logging.debug('Started in debug mode')
    logging.warning('Started in warning mode')
    do_something()
    logging.info('Finished')

if __name__ == '__main__':
    lib.logger.setup_logging()
    main()
