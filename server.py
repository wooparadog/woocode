#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
server.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2011-11-19
'''

import tornado.httpserver
import tornado.web

from _url import URL_HANDLERS
import url 
from config import PORT, ROOT


class MainPage(tornado.web.RequestHandler):
    def get(self):
        self.write('out')

def main():
    application = tornado.web.Application(URL_HANDLERS)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
