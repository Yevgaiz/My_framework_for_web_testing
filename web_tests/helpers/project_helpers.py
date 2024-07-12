import configparser
import os


def get_project_root():
    return os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]


def get_config_path():
    return os.path.join(get_project_root(), 'config.ini')


def get_parser():
    config = configparser.ConfigParser()
    config.read(get_config_path())
    return config


def get_base_url():
    parser = get_parser()
    return parser['test']['base_url']


def get_browser():
    parser = get_parser()
    return parser['test']['browser'].lower()
