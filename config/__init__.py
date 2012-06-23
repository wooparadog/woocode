#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__init__.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''

import tornado.wsgi
import mako.lookup
import os
import sys
from os.path import abspath,dirname,join
from private_config import CONNECTION_STRING
import dependencies.git_http_backend.git_http_backend


OWN_SITE = ['account', 'repos']
RESERVED_PATH = '|'.join(OWN_SITE)
SITE_DOMAIN = "il3v0u4v3r"
SITE_LINK = "http://%s/%%s"%SITE_DOMAIN
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_PATH = join(ROOT,"static/upload")
PORT = 8080

TEMPLATE_LOOKER = mako.lookup.TemplateLookup([join(ROOT,'templates')])

DATABASE_TABLES = { 'main': ['repos','*'] }
DATABASE_CONNECTION = CONNECTION_STRING
DATABASE_CONFIG = {
        "main": {
            "master": DATABASE_CONNECTION,
            "tables": DATABASE_TABLES['main'],
            },
        }
STATIC_DOMAIN = "http://s.%s/%%s"%SITE_DOMAIN

REPO_PATHS = os.path.join(ROOT,'repos')
git_app = dependencies.git_http_backend.git_http_backend.assemble_WSGI_git_app(
        content_path = REPO_PATHS,
        repo_auto_create = True
)
git_app = tornado.wsgi.WSGIContainer(git_app)

def render(self,template_name=None,**kargs):
    template = None
    if template_name:
        template = TEMPLATE_LOOKER.get_template(template_name)
    else:
        template = TEMPLATE_LOOKER.get_template(self.__class__.__name__+'.html')
    if template:
        return self.write(template.render(**kargs))
