# coding=utf-8
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
from os.path import abspath, realpath, dirname
from configparser import ConfigParser


BASE_DIR = abspath(dirname(__file__))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# get the files path
file_dir_path = dirname(realpath(__file__))
config_parser = ConfigParser()
config_file = file_dir_path + "/config.ini"
config_parser.read(config_file)

# API version
API_PREFIX = config_parser.get("api_info", "prefix")
API_VERSION = config_parser.get("api_info", "version")

# DB config
DB_NAME = config_parser.get("db", "db_name").strip()
DB_USER = config_parser.get("db", "db_user").strip()
DB_PASSWORD = config_parser.get("db", "db_password").strip()
DB_HOST = config_parser.get("db", "db_host").strip()
DB_PORT = config_parser.get("db", "db_port").strip()
