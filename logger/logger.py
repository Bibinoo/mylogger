import os, sys
import logging.config
import yaml

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
    def change_value(self, key_searched, change_value, function_name=None):
        # parsing the dictionary
        for k, value in self.items():

            # checking if the value is a dictionary
            if isinstance(value, dict):
                # recursive function to find searched keys
                self[k] = ObjDict(value).change_value(key_searched, change_value, function_name)

        if key_searched in self:

            # if no other method than change_value is called
            if function_name is None:
                # replace the value of the searched key from a dictionary
                self[key_searched] = change_value

            # if method insert_value is called
            elif function_name == 'insert_value':
                # insert a string before the value of the searched key
                # from a dictionary
                self[key_searched] = change_value + self[key_searched]

            # if method append_value is called
            elif function_name == 'append_value':
                # append a string after the value of the searched key
                # from a dictionary
                self[key_searched] = self[key_searched] + change_value
        return self

    # insert a string in the value of a key in a nested dictionary
    def insert_value(self, key_searched, string_to_insert):
        # store the function name in a variable to simplify the code reading
        function_name = ObjDict.insert_value.__name__
        # simplify the code reading
        change_value = string_to_insert
        # assign the result of recursive function
        self = ObjDict.change_value(self, key_searched, change_value,
               function_name)
        return self

    # append a string in the value of a key in a nested dictionary
    def append_value(self, key_searched, string_to_append):
        # store the function name in a variable to simplify the code reading
        function_name = ObjDict.append_value.__name__
        # simplify the code reading
        change_value = string_to_append
        # assign the result of recursive function
        self = ObjDict.change_value(self, key_searched, change_value,
               function_name)
        return self

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

        # Replace the value of the key filename by default path
        instance = ObjDict(config)
        # print("default_path", default_path)
        config = instance.insert_value('filename', default_path + "\\")

        # Amend the logging level to DEBUG
        if default_level == "logging.DEBUG":
            config = instance.change_value('level', "DEBUG")

        # loading the configuration dictionary
        logging.config.dictConfig(config)

        # check if the path where logs needs to be written exists
        logging.getLogger(__name__).info('Loaded ' + logconf_path +
            ' configuration file for logger!')

        # print out the configuration in debug mode only
        logging.getLogger(__name__).debug(config)

    else:
        # Configure basics when the configuration file cannot be loaded
        logging.basicConfig(level=default_level)
        logging.getLogger(__name__).warning('Failed to load ' + logconf_path +
            ' configuration file for logger!')
