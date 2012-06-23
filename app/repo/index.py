#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _url import addHandlers  
from _base import baseHandler
from model.repo import Repo, create_new_repo
from model.user import User
from config import RESERVED_PATH


@addHandlers(r'^/repos/new$')
class Index(baseHandler):
    def get(self):
        self.render("/app/repo/new.html")

    def post(self):
        #TODO: hey, add user?!!!
        user = self.get_argument("user", 'wooparadog')
        user = User.get(name=user)
        repo_name = self.get_argument("name", None)
        repo_desc = self.get_argument("desc", None)

        re_dir = create_new_repo(user=user, name=repo_name, desc=repo_desc)
        self.redirect(re_dir.link)


@addHandlers(r'^/((?!%s)[a-zA-Z0-9]+)/([a-zA-Z0-9]+)$'%RESERVED_PATH)
class Index(baseHandler):
    def get(self, username, repo):
        user = User.where(name=username)
        if user:
            user = user[0]
            repo = Repo.where(owner_id=user.id, name=repo)
            if repo:
                repo = repo[0]
                self.render("/app/repo/repo.html", repo=repo)
