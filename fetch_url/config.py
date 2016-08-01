"""Configuration for fetch-url agent."""
from os import environ
from config_common import NAME_SEPARATOR, AGENT_NAME, AGENT_SUFFIX,\
    STORE_URL, STORE_CONFIG_DB, PAGE_TYPE

AGENT_TYPE = 'fetch'
SERVICE_NAME = 'fetch_page_tos'

# configuration that depends on common constants
STORE_DB = environ.get('STORE_CONFIG_DOC') or \
    NAME_SEPARATOR.join([AGENT_NAME, AGENT_SUFFIX])
STORE_DB_URL = '/'.join([STORE_URL, STORE_DB])
STORE_LATEST_VIEW = '_design/page/_view/latest?reduce=true&group_level=2&' \
    'startkey=["page","' + PAGE_TYPE + '","%s"]' \
    '&endkey=["page","' + PAGE_TYPE + '","%s",{}]'
STORE_LATEST_VIEW_URL = '/'.join([STORE_DB_URL, STORE_LATEST_VIEW])
# https://staging-store.openintegrity.org/pages-juga/_design/page/_view/latest?reduce=true&group_level=2&startkey=["page","tos","https://guardianproject.info/home/data-usage-and-protection-policies/"]&endkey=["page","tos","https://guardianproject.info/home/data-usage-and-protection-policies/",{}]

STORE_UPDATE_DOC = "_design/page/_update/timestamped/%s"
STORE_UPDATE_DOC_URL = '/'.join([STORE_DB_URL, STORE_UPDATE_DOC])

STORE_CONFIG_DOC = environ.get('STORE_CONFIG_DOC') or \
                    NAME_SEPARATOR.join([AGENT_NAME, AGENT_SUFFIX])
STORE_CONFIG_URL = '/'.join([STORE_URL, STORE_CONFIG_DB, STORE_CONFIG_DOC])
# STORE_CONFIG_URL = https://staging-store.openintegrity.org/config/pages-juga

# configuration specific for fech
###################################
ANALYSE_PAGE_HOST = environ.get('ANALYSE_PAGE_HOST')
ANALYSE_PAGE_PORT = environ.get('ANALYSE_PAGE_PORT')
if ANALYSE_PAGE_HOST and ANALYSE_PAGE_PORT:
    ANALYSE_PAGE_DOMAIN = 'http://' + ":".join([ANALYSE_PAGE_HOST, ANALYSE_PAGE_PORT])
else:
    ANALYSE_PAGE_DOMAIN = 'http://127.0.0.1:8002'
ANALYSE_PAGE_NAME = 'analyse_page_tos'
ANALYSE_PAGE_URL = '/'.join([ANALYSE_PAGE_DOMAIN, ANALYSE_PAGE_NAME])
