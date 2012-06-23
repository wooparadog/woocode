#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
_base.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''

from config import render
import tornado.web

class baseHandler(tornado.web.RequestHandler):
    render = render
