import os, sys
import logging.config
import yaml

# sys.path.append("C:\\Users\\denny_000\\Documents\\GitHub\\outlook")
print(sys.path[0])
def setup_logging(default_path = 'conf/log_conf.yaml', default_level = logging.INFO,
    env_key = 'LOG_CFG'):

    """
        Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def do_something():
    logging.info('Doing something')


def main():
    logging.info('Started')
    logging.debug('Started in debug mode')
    do_something()
    logging.info('Finished')

if __name__ == '__main__':
    setup_logging()
    main()
