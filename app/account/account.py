#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _url import addHandlers  
from _base import baseHandler
from model.repo import Repo, create_new_repo
from model.user import User, create_new_user, login_user
from config import RESERVED_PATH, SESSION_KEY



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

@addHandlers(r'^/account/login')
class Index(baseHandler):
    def get(self):
        if not self.current_user:
            self.render("/app/account/login.html")
        else:
            self.redirect('/')

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        cookie = login_user(username, password)
        if cookie:
            self.set_cookie(SESSION_KEY, cookie)
            return self.redirect("/")
        raise
