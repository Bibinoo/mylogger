import os, sys
import logging.config
import yaml

# Setting up the logger configuration
def setup_logging(default_path = 'data/log_conf.yaml', default_level = logging.INFO,
    env_key = 'LOG_CFG'):

    # Input default configuration file
    path = default_path

    # Input the configuration file from the command line
    value = os.getenv(env_key, None)
    if value:
        path = value

    # Read and load the configuration file
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        logging.getLogger(__name__).info('Loaded ' + path + ' logger configuration!')
    else:
        logging.basicConfig(level=default_level)
        logging.getLogger(__name__).warning('Failure to load ' + path + ' logger configuration!')
