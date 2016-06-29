"""fetch_url."""
from nameko.web.handlers import http
from werkzeug.wrappers import Response
from werkzeug import exceptions
from os.path import join
import json
import yaml
import logging
import logging.config
# from logger import LoggingDependency
from config import CONFIG, FS_PATH, ANALYSE_URL
try:
    from agents_common.etag_requests import get_ismodified
    from agents_common.policies_util import generate_hash
    from agents_common.scraper_utils import url2filename
except:
    from config import AGENTS_MODULE_PATH
    import sys
    sys.path.append(AGENTS_MODULE_PATH)
    from agents_common.etag_requests import get_ismodified
    from agents_common.policies_util import generate_hash
    from agents_common.scraper_utils import url2filename
from fetch_utils import retrive_hash_store, store_html, analyse_url

logging.basicConfig(level=logging.DEBUG)
with open(CONFIG) as fle:
    config = yaml.load(fle)
if "LOGGING" in config:
    logging.config.dictConfig(config['LOGGING'])
logger = logging.getLogger(__name__)


class FetchURLService(object):
    name = "fetchurl"


    # FIXME: temporally getting the values as POST data cause string:url
    # causes 409
    @http('POST', '/fetchurl')
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
        # logger.debug('request form : %s', request.form)
        # logger.debug('request values : %s', request.values)
        # logger.debug('request data : %s', request.data)
        url = json_data.get('key')
        logger.debug('key: %s', url)
        header = json_data.get('header')
        content = json_data.get('content')
        logger.debug('type content %s', type(content))
        if content:
            logger.debug("len content %s", len(content))
        if header:
            etag = header.get('ETag')
            logger.debug('etag: %s', etag)
            last_modified = header.get('Last-Modified')
            logger.debug('last_modified: %s', last_modified)
            # print request.data
            # content = request.get_data('content', as_text=True)
            # content = request.values.get('content')
        ismodified, r = get_ismodified(
                                        url, etag=etag,
                                        last_modified=last_modified)
        if ismodified:
            # get content in unicode, either of this works
            unicode_content = unicode( r.content, r.encoding )
            unicode_content = r.text
            hash_page_html = generate_hash(unicode_content, r.encoding)
            filepath = join(FS_PATH, url2filename(url) + hash_page_html)
            hash_in_fs = retrive_hash_store(filepath)
            if not hash_in_fs:
                logger.info('hash is not in the file system')
                store_html(filepath, content)
                analyse_url(ANALYSE_URL, url, hash_page_html, etag,
                            last_modified)
            return Response(json.dumps({'url': url}))
