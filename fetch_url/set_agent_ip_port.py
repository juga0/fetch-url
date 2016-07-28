#!/usr/bin/env python
"""Script to setup the host and port for the agent service. """
import yaml
from os import environ

with open('config.yml') as f:
    s = f.read()
    c = yaml.load(s)
# if there is an environment variable, write it in the nameko config file
# WEB_SERVER_ADDRESS = environ.get('WEB_SERVER_ADDRESS')
FETCH_PAGE_HOST = environ.get('FETCH_PAGE_HOST')
FETCH_PAGE_PORT = environ.get('FETCH_PAGE_PORT')
if FETCH_PAGE_HOST and FETCH_PAGE_PORT:
    WEB_SERVER_ADDRESS = ":".join(["http://",
                                   FETCH_PAGE_HOST, FETCH_PAGE_PORT])
if WEB_SERVER_ADDRESS:
    c['WEB_SERVER_ADDRESS'] = WEB_SERVER_ADDRESS
    with open('config.yml', 'w') as f:
        s = yaml.dump(c)
        f.write(s)
else:
    # check that the key is in the file
    WEB_SERVER_ADDRESS = c.get(WEB_SERVER_ADDRESS)
    if WEB_SERVER_ADDRESS is None:
        WEB_SERVER_ADDRESS = '127.0.0.1:8000'
        c['WEB_SERVER_ADDRESS'] = WEB_SERVER_ADDRESS
        with open('config.yml', 'w') as f:
            s = yaml.dump(c)
            f.write(s)
