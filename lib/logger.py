import os, sys
import logging.config
import yaml

print (os.path.dirname(__file__))

# Recursively replace dictionary values with matching key
def replace_dictitem(obj, key, replace_value):
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = replace_dictitem(v, key, replace_value)
    if key in obj:
        print(obj[key])
        obj[key] = replace_value
        print(obj[key])
    return obj

# to implement in the function
def get_yaml_config(path):
    try:
        with open(path, 'r') as file:
            logconf = yaml.safe_load(file)
    except FileNotFoundError:
        return {}
    return logconf

# More reference here: https://docs.python.org/3/howto/logging-cookbook.html
# Setting up the logger configuration
# If no argument, take by default path, logconf, level and envkey
def setup_logging(default_path = 'conf/', default_logconf = 'log_conf.yaml' ,
    default_level = logging.INFO, default_envkey = 'LOG_CFG'):

    # Built the full path of the configuration file
    logconf_path = default_path + "\\" + default_logconf

    # Input the configuration file from the command line
    # Not really tested at this point of time
    envkey_value = os.getenv(default_envkey, None)
    if envkey_value:
        logconf_path = envkey_value

    # Read and load the configuration file
    if os.path.exists(logconf_path):
        with open(logconf_path, 'rt') as file:
            config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)

        replace_dictitem(config, 'filename', 'new path name')

        logging.getLogger(__name__).info('Loaded ' + logconf_path +
            ' configuration file for logger!')
    else:
        # Configure basics when the configuration file cannot be loaded
        logging.basicConfig(level=default_level)
        logging.getLogger(__name__).warning('Failed to load ' + logconf_path +
            ' configuration file for logger!')
