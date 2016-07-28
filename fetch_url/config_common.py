"""Common configuration for watch/fetch/analyse-page-tos agents."""
# urljoin only join with one argument
# from urlparse import urljoin
from os.path import join, abspath, dirname
from os import environ

AGENT_NAME = 'page-tos'
AGENT_SUFFIX = 'juga'
NAME_SEPARATOR = '-'
# this will be overwroten by the config interval in the store
INTERVAL = 10
# KEY = ['policies', 'urls']
KEY = 'config'

# paths
############################
BASE_PATH = abspath(__file__)
# BASE_PATH = abspath('.')
ROOT_PATH = dirname(BASE_PATH)
PROJECT_PATH = dirname(ROOT_PATH)
ROOT_PROJECT_PATH = dirname(PROJECT_PATH)
# in case agents-common-code is not installed, the path to it is requered
AGENTS_MODULE_DIR = 'agents-common-code'
AGENTS_MODULE_PATH = join(ROOT_PROJECT_PATH, AGENTS_MODULE_DIR)

# fs store
FS_PATH = join(PROJECT_PATH, 'data')

# URLs
############################
# couchdb configuration and urls
STORE_URL = 'https://staging-store.openintegrity.org'
STORE_CONFIG_DB = environ.get('STORE_CONFIG_DB') or 'config'

# data
############################
AGENT_PAYLOAD = """{
    "key": "%(key)",
    "agent_ip": "%(agent_ip)",
    "agent_type": "%(agent_type)",
    "header": {
        "etag": "%(etag)",
        "last-modified": "%(last_modified)"
    },
    "content": "%(content)"
}"""
