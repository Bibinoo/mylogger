import os, sys
import logging.config
import yaml
#import curses

print (os.path.dirname(__file__))

#curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
#stdscr.addstr(0, 0, 'hello', curses.color_pair(1))
# This class is working but may be dangerous
class WorkingObjDict():
    def __init__(self, dictionary=None):
        if dictionary is None:
            pass
        elif isinstance(dictionary, dict):
            self.__dict__.update(dictionary)
            #print(self.__dict__)
        else:
            raise TypeError('A dictionary is expected as an argument')

    def replace_value(self, key_searched, new_value):
        for k, value in self.__dict__.items():
            # Recursive method
            if isinstance(value, dict):
                self.__dict__[k] = ObjDict(value).replace_value(key_searched, new_value)
        if key_searched in self.__dict__:
            # replace the value
            self.__dict__[key_searched] = new_value
        return self.__dict__

class ObjDict(dict):
    def replace_value(self, key_searched, new_value):
        for k, value in self.items():
            if isinstance(value, dict):
                self[k] = ObjDict(value).replace_value(key_searched, new_value)
        if key_searched in self:
            # replace the value
            self[key_searched] = new_value
        return self

# Recursively replace dictionary values with matching key
def replace_dictitem(obj, key, new_value):
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = replace_dictitem(v, key, new_value)
    if key in obj:
        print(obj[key])
        # replace the value
        obj[key] = new_value
        print(obj[key])
        # insert a value
        obj[key] = 'insert value: ' + new_value
        print(obj[key])
        # append a value
        obj[key] = new_value + ' :append value'
        # delete the key
        # del obj[key]
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

        # Replace the value of the key filename by default path
        instance = ObjDict(config)
        config = instance.replace_value('filename', default_path + "\\")
        print(config)
        logging.getLogger(__name__).info('Loaded ' + logconf_path +
            ' configuration file for logger!')
    else:
        # Configure basics when the configuration file cannot be loaded
        logging.basicConfig(level=default_level)
        logging.getLogger(__name__).warning('Failed to load ' + logconf_path +
            ' configuration file for logger!')
