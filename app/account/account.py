#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _url import addHandlers  
from _base import baseHandler
from model.repo import Repo, create_new_repo
from model.user import User, create_new_user
from config import RESERVED_PATH


@addHandlers(r'^/account/register')
class Register(baseHandler):
    def get(self):
        self.render("/app/account/register.html")

    def post(self):
        user = self.get_argument("username", None)
        email = self.get_argument("email" , None)
        password = self.get_argument("password", None)
        password2 = self.get_argument("password2", None)
        if all([user, email, password, password2]):
            user = create_new_user(user, email, password, password2)
            if user:
                self.redirect(user.link)


@addHandlers(r'^/((?!%s)[a-zA-Z0-9]+)$'%RESERVED_PATH)
class Index(baseHandler):
    def get(self, username):
        user = User.get(name=username)
        if user:
            self.render("/app/account/index.html", user=user)
        
