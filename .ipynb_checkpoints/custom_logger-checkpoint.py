import sys
import logging

sys.path.append("C:\\Users\\denny_000\\Documents\\GitHub\\outlook")
import config

def do_something():
    logging.info('Doing something')

def main():
    logging.info('Started')
    do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
    for key, value in config.DevConfig.LOGGER_CONFIG.items() :
        print (key, value)
