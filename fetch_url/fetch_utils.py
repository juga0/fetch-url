"""Util functions for fetch-url."""
from os.path import join, isfile, isdir, dirname
from os import makedirs
import requests
import logging

logger = logging.getLogger(__name__)
# print 'LOG LEVEL fetch_utils'
# print logging.getLevelName(logger.getEffectiveLevel())

def retrieve_hash_store(filepath):
    """
    """
    # filepath = join(dirpath, url + hash_content)
    logger.debug('checking whether %s exists', filepath)
    if isfile(filepath):
        logger.debug('file exists')
        return True
    return False


def save_content_store(filepath, content, encoding='utf-8'):
    """
    """
    logger.debug('writing content to %s', filepath)
    logger.debug('content type %s', type(content))
    if not isdir(dirname(filepath)):
        logger.debug('creating dir %s', dirname(filepath))
        makedirs(dirname(filepath))
    with open(filepath, 'w') as f:
        f.write(content.encode(encoding))


def post_store(url, data, only_status_code=False):
    logger.debug('POST url %s' % url)
    if isinstance(data, dict):
        r = requests.post(url, json=data)
    else:
        r = requests.post(url, data=data)
    if only_status_code:
        return r.status_code
    return r


# def analyse_url(url_analyse_url, url, hash_content, etag, last_modified):
def analyse_url(url, data):

    """
    """
    # data = {
    #     'url': url,
    #     'hash': hash_content,
    #     'etag': etag,
    #     'last_modified': last_modified
    # }
    return post_store(url, data, only_status_code=True)
