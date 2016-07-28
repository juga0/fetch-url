"""fetch_url."""
import sys
import json
import logging
import logging.config

from nameko.web.handlers import http
from werkzeug.wrappers import Response
from werkzeug import exceptions
from os.path import join

try:
    from agents_common.etag_requests import get_ismodified
    from agents_common.policies_util import generate_hash
    from agents_common.scraper_utils import url2filenamedashes
except:
    from config import AGENTS_MODULE_PATH
    sys.path.append(AGENTS_MODULE_PATH)
    from agents_common.etag_requests import get_ismodified
    from agents_common.policies_util import generate_hash
    from agents_common.scraper_utils import url2filenamedashes

from config import ANALYSE_PAGE_URL, SERVICE_NAME
from config_common import FS_PATH

from fetch_utils import retrieve_hash_store, save_content_store, analyse_url

logging.basicConfig(level=logging.DEBUG)
try:
    from config import LOGGING
    logging.config.dictConfig(LOGGING)
except ImportError:
    print "Couldn't find LOGGING in config.py"
logger = logging.getLogger(__name__)


class FetchURLService(object):
    name = SERVICE_NAME

    # FIXME: temporally getting the values as POST data cause string:url
    # causes 409
    # TODO: handle errors
    # TODO: use nameko events
    @http('POST', '/' + SERVICE_NAME)
    def fetch_url(self, request):
        """
        """
        if request.method != "POST":
            raise exceptions.MethodNotAllowed
        logger.debug('request: %s', request)
        # FIXME: is this the best way to obtain post payload?
        #        or should insted use .form or .vaules or .data?
        data = request.get_data()
        logger.debug('data %s', data)
        json_data = json.loads(data)
        logger.debug('json data %s', json_data)
        url = json_data.get('key')
        logger.debug('key: %s', url)
        header = json_data.get('header')
        # NOTE: the content is not needed
        # content = json_data.get('content')
        # logger.debug('type content %s', type(content))
        # if content:
        #     logger.debug("len content %s", len(content))
        if header:
            etag = header.get('etag')
            logger.debug('etag: %s', etag)
            last_modified = header.get('last_modified')
            logger.debug('last_modified: %s', last_modified)
        ismodified, r = get_ismodified(url, etag=etag,
                                       last_modified=last_modified)
        if ismodified:
            # NOTE: get content in unicode, either of this works
            # unicode_content = unicode( r.content, r.encoding )
            unicode_content = r.text
            hash_html = generate_hash(unicode_content, r.encoding)
            html_filepath = join(FS_PATH, url2filenamedashes(url),
                                 hash_html + '.html')
            hash_in_fs = retrieve_hash_store(html_filepath)
            if not hash_in_fs:
                logger.info('Hash is not in the file system.')
                save_content_store(html_filepath, unicode_content)
                # TODO: if in watch the trigger url is obtain from config
                # where the url for analyse will be get?
                # FIXME: remove hash in the data
                json_data['sha256'] = hash_html
                # FIXME: pass here all the dict as in watch_url
                # r = analyse_url(ANALYSE_PAGE_URL, url, hash_html, etag,
                #                 last_modified)
                logger.debug('Going to request analyse_url %s' %
                             ANALYSE_PAGE_URL)
                r = analyse_url(ANALYSE_PAGE_URL, json_data)
                if r != 200:
                    sys.exit()
            return Response(status=200)

# TODO: add main
