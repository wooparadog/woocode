#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _url import addHandlers  
from _base import baseHandler
from model.repo import Repo

@addHandlers(r'^/')
class rootIndex(baseHandler):
    def get(self):
        self.write("HELLOWORLD")
