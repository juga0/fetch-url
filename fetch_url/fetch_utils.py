"""Util functions for fetch-url."""
from os.path import join, isfile, isdir, dirname
from os import makedirs
import requests
import logging

logger = logging.getLogger(__name__)


def retrive_hash_store(filepath):
    """
    """
    # filepath = join(dirpath, url + hash_content)
    logger.debug('checking whether %s exists', filepath)
    if isfile(filepath):
        logger.info('html with with path %s exists', filepath)
        return True
    return False


def store_html(filepath, content):
    """
    """
    # filepath = join(dirpath, url + hash_page_html)
    if not isdir(dirname(filepath)):
        logger.debug('creating dir %s', dirname(filepath))
        makedirs(dirname(filepath))
    logger.debug('writing content to %s', filepath)
    with open(filepath, 'w') as f:
        f.write(content)


def analyse_url(url, hash_content):
    """
    """
    complete_url = '/'.join([url, hash_content])
    logger.debug('get url %s with sha %s' % (url, hash_content))
    r = requests.get(complete_url)
    return r.status_code


def scraper_rule(rule_json):
    page = requests.get(rule_json['url'])
    tree = html.fromstring(page.content)
    e = tree.xpath(rule_json['xpath'])
    html_text = etree.tostring(e[0])
    md = html2md(html_text)
    return mddef scraper_tos(rules_json):
    for rule_json in rules_json:
        scraper_rule(rule_json)
