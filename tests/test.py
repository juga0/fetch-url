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
    # payload = '{"xpath": "//article", "agent_ip": "78.142.19.213", "content": "", "header": {"etag": "", "last_modified": ""}, "agent_type": "watch", "page_type": "tos", "key": "https://guardianproject.info/home/data-usage-and-protection-policies/", "timestamp_measurement": "2016-07-29T23:13:15.511Z", "sha256": "577cd1563b7d08dea2864cad528bdc3d3b8ab64e1ecd49a092e95535e9d1cdcc"}'
    # payload = {
    #     u'attribute': u'page/content',
    #     u'context': {
    #         u'agent_ip': u'185.69.168.112',
    #         u'agent_type': u'watch',
    #         u'page_type': u'tos',
    #         u'timestamp_measurement': u'2016-08-04T01:06:18.125782Z',
    #         u'xpath': u'//article'
    #     },
    #     u'entity': u'https://guardianproject.info/home/data-usage-and-protection-policies/',
    #     u'value': {
    #         u'header': {
    #             u'etag': u'',
    #             u'last_modified': u''
    #         },
    #         "sha256_html": "577cd1563b7d08dea2864cad528bdc3d3b8ab64e1ecd49a092e95535e9d1cdcc"
    #     }
    # }
    payload = {'attribute': 'page/content', 'value': {'header': {'last-modified': 'Mon, 01 Sep 1997 01:03:33 GMT', 'etag': 'None'}, 'sha256_html': '8626313e98732160ceb314ca1e6160697cd190d953974e2000802ff63eaf405c'}, 'context': {'xpath': "//div[@id='body']", 'timestamp_measurement': '2016-08-05T13:58:59.114779Z', 'agent_type': 'watch', 'page_type': 'tos', 'agent_ip': '46.166.188.203'}, 'entity': 'http://www.t-mobile.com/Templates/Popup.aspx?PAsset=Ftr_Ftr_TermsAndConditions&amp;print=true'}
    return_value = 200
    r = analyse_url(ANALYSE_PAGE_URL, payload)
    assert return_value == r
