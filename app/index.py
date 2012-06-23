#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _url import addHandlers  
from _base import baseHandler
from model.repo import Repo, create_new_repo
from model.user import User

@addHandlers(r'^/')
class Index(baseHandler):
    def get(self):
        all_repos = Repo.where()
        self.render("/app/index.html",  all_repos=all_repos)
