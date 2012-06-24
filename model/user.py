#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _base import Model, McModel
from config import SITE_LINK

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


def create_new_user(user, email, password, password2):
    if password == password2:
        new_user = User()
        new_user.name = user
        new_user.password = password
        new_user.email = email
        new_user.save()
        return new_user

if __name__ == '__main__':
    create_new_user('wooparadog', 'guohaochuan@gmail.com', 'abc', 'abc')
