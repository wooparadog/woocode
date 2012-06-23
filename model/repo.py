#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path as path
from subprocess import check_call
from _base import Model, McModel
from config import REPO_PATHS

class Repo(McModel):
    pass

def create_new_repo(user, name):
    repo_path = path.join(REPO_PATHS, user.name, name)
    check_call(('git init %s'%repo_path).split())
    new_repo = Repo()
    new_repo.user_id = user.id
    new_repo.path = repo_path
    new_repo.name = name
    new_repo.save()

if __name__ == '__main__':
    from user import User
    user = User.where(name="wooparadog")
    if user:
        user = user[0]
        create_new_repo(user, "hello_world")

