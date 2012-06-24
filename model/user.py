#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from _base import Model, McModel
from config import SITE_LINK
from session import set_user_session

class User(McModel):
    @property
    def link(self):
        return SITE_LINK%self.name

    @property
    def repos(self):
        from repo import Repo
        return Repo.where(owner_id=self.id)

    @property
    def n_repos(self):
        return len(self.repos)

def login_user(username, password):
    user = verify_user_by_username(username, password)
    if user:
        secret = set_user_session(user)
        return '%s:%s'%(user.id, secret)

def verify_user_by_username(username, password):
    user = User.get(name=username)
    if user:
        if verify_user_by_user(user, password):
            return user

def verify_user_by_user_id(user_id, password):
    user = User.mc_get(user_id)
    if user:
        return verify_user_by_user(user, user_id)

def verify_user_by_user(user, password):
    if pwd_hash2(user.email, password) == user.password:
        return user

def pwd_hash2(email, password):
    if not password:
        return ''
    m = hashlib.md5(email.lower())
    m.update(password)
    return m.hexdigest()[:15]

def create_new_user(user, email, password, password2):
    if password == password2:
        new_user = User()
        new_user.name = user
        new_user.password = pwd_hash2(email, password)
        new_user.email = email
        new_user.save()
        return new_user

if __name__ == '__main__':
    create_new_user('wooparadog', 'guohaochuan@gmail.com', 'abc', 'abc')
