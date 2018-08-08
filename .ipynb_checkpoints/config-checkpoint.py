# config.py

class Config:
    LOGGER_CONFIG = {
        'filename': 'log/error.log',
        'filemode': 'a' # a for appending mode, w for a fresh log
    }

class DevConfig(Config):
    LOGGER_CONFIG = {
        'level': 'INFO'
    }

class ProdConfig(Config):
    LOGGER_CONFIG = {
        'level': 'INFO'
    }
