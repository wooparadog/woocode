#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path as path
from subprocess import check_call
from _base import Model, McModel
from config import REPO_PATHS, SITE_LINK
from user import User

class Repo(McModel):
    @property
    def abs_path(self):
        return path.join(REPO_PATHS, self.owner.name, self.name)

    @property
    def link(self):
        return SITE_LINK%path.join(self.owner.name, self.name)

    @property
    def clone_addr(self):
        return self.link + '.git'

    @property
    def owner(self):
        return User.get(self.owner_id)



def create_new_repo(user, name, desc):
    repo_path = path.join(REPO_PATHS, user.name, name) + ".git"
    check_call(('git init %s'%repo_path).split())
    new_repo = Repo()
    new_repo.owner_id = user.id
    new_repo.path = repo_path
    new_repo.name = name
    new_repo.desc = desc
    new_repo.save()
    return new_repo

if __name__ == '__main__':
    from user import User
    user = User.where(name="wooparadog")
    if user:
        user = user[0]
        new_repo = create_new_repo(user, "hello_world", "null")
        print new_repo.name
        print new_repo.owner.name
        print new_repo.link
        print new_repo.abs_path

