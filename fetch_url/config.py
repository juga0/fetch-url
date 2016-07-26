"""Configuration for fetch-url agent."""
from os.path import join, abspath, dirname

BASE_PATH = abspath(__file__)
# BASE_PATH = abspath('.')
ROOT_PATH = dirname(BASE_PATH)
PROJECT_PATH = dirname(ROOT_PATH)
ROOT_PROJECT_PATH = dirname(PROJECT_PATH)
# in case agents-common-code is not installed, the path to it is requered
AGENTS_MODULE_DIR = 'agents-common-code'
AGENTS_MODULE_PATH = join(ROOT_PROJECT_PATH, AGENTS_MODULE_DIR)

AGENT_TYPE = 'fetch-url'
SERVICE_NAME = 'fetchurl'

FS_PATH = join(PROJECT_PATH, 'data')

# analyse-url configuration
# FIXME: temporal url for development
ANALYSE_PAGE_DOMAIN = 'http://127.0.0.1:8002'
ANALYSE_PAGE_NAME = 'analyseurl'
ANALYSE_PAGE_URL = '/'.join([ANALYSE_PAGE_DOMAIN, ANALYSE_PAGE_NAME])

# rabbitmq configuration
AMQP_CONFIG = {'AMQP_URI': 'amqp://guest:guest@localhost'}

# logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': "%(levelname)s:%(name)s - %(module)s - %(message)s"
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    # 'loggers': {
    #     'nameko': {
    #         'level': 'DEBUG',
    #         'handlers': ['console']
    #     }
    # },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}
