""" Unit testing...
"""
# run with  py.test -s tests/test.py

import sys
import json
import logging

from os.path import join
import logging.config

from nameko.web.handlers import http
from werkzeug.wrappers import Response
from werkzeug import exceptions

try:
    from agents_common.etag_requests import get_ismodified
    from agents_common.policies_util import generate_hash
    from agents_common.scraper_utils import url2filenamedashes
except ImportError:
    print('agents_common is not installed '
          'or does not contain one of the required modules,'
          ' trying to find it inside this program path')
    try:
        from config import AGENTS_MODULE_PATH
        sys.path.append(AGENTS_MODULE_PATH)
        from agents_common.etag_requests import get_ismodified
        from agents_common.policies_util import generate_hash
        from agents_common.scraper_utils import url2filenamedashes
    except ImportError:
        print('agents_common not found in this program path, '
              'you need to install it or'
              ' create a symlink inside this program path')
        sys.exit()

from fetch_url.config import ANALYSE_PAGE_URL, SERVICE_NAME
from fetch_url.config_common import FS_PATH

from fetch_url.fetch_utils import retrieve_hash_store, save_content_store, analyse_url


try:
    from config_common import LOGGING
    logging.config.dictConfig(LOGGING)
except ImportError:
    print "Couldn't find LOGGING in config.py"
    logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_analyse_url():
    url_analyse = 'http://127.0.0.1:8002/analyse_page_tos'
    assert ANALYSE_PAGE_URL == url_analyse


def test_post_url():
    payload = '{"xpath": "//article", "agent_ip": "78.142.19.213", "content": "", "header": {"etag": "", "last_modified": ""}, "agent_type": "watch", "page_type": "tos", "key": "https://guardianproject.info/home/data-usage-and-protection-policies/", "timestamp_measurement": "2016-07-29T23:13:15.511Z", "sha256": "577cd1563b7d08dea2864cad528bdc3d3b8ab64e1ecd49a092e95535e9d1cdcc"}'
    return_value = 200
    r = analyse_url(ANALYSE_PAGE_URL, payload)
    assert return_value == r
