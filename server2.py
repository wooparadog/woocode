#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import web
from tornado import httpserver
from tornado import ioloop
import tornado.wsgi
import os
import dependencies.git_http_backend.git_http_backend
from config import REPO_PATHS

app = web.Application([
    ('/.*\.git/.*', tornado.web.FallbackHandler, dict(fallback=git_app)),
    ], debug=True)

def main():
    server = httpserver.HTTPServer(app)
    server.listen(8080)
    ioloop.IOLoop().instance().start()


if __name__ == '__main__':
    main()
