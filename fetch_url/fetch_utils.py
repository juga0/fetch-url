"""Util functions for fetch-url."""
from os.path import join, isfile, isdir, dirname
from os import makedirs
import requests
import logging

logger = logging.getLogger(__name__)


def retrieve_hash_store(filepath):
    """
    """
    # filepath = join(dirpath, url + hash_content)
    logger.debug('checking whether %s exists', filepath)
    if isfile(filepath):
        return True
    return False


def save_content_store(filepath, content, encoding='utf-8'):
    """
    """
    # filepath = join(dirpath, url + hash_page_html)
    if not isdir(dirname(filepath)):
        logger.debug('creating dir %s', dirname(filepath))
        makedirs(dirname(filepath))
    logger.debug('writing content to %s', filepath)
    with open(filepath, 'w') as f:
        f.write(content.encode(encoding))

def analyse_url(url_analyse_url, url, hash_content, etag, last_modified):
    """
    """
    # complete_url = '/'.join([url, hash_content])
    # logger.debug('get url %s with sha %s' % (url, hash_content))
    # r = requests.get(complete_url)
    data = {
        'url': url,
        'hash': hash_content,
        'etag': etag,
        'last_modified': last_modified
    }
    r = requests.post(url_analyse_url, json=data)
    return r.status_code
