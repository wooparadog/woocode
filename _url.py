#!/usr/bin/env python
# -*- coding: utf-8 -*-

URL_HANDLERS = []

def addHandlers(url):
    def _(cl):
        URL_HANDLERS.append((url,cl))
    return _
