########################################################################################################################
# IMPORTS

import configparser
import logging


########################################################################################################################
# FUNCTIONS

def get_config(config_path):
    cfg = configparser.RawConfigParser()
    cfg.read(config_path)
    return cfg


def get_logger(level):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(level.upper())
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
