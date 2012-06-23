#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
_url.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''
import tornado.web
from config import git_app

URL_HANDLERS = [
        ('/.*\.git/.*', tornado.web.FallbackHandler, dict(fallback=git_app)),
        ]

def addHandlers(url):
    def _(cl):
        URL_HANDLERS.append((url,cl))
    return _
