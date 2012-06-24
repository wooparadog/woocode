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
    def repo_path(self):
        return self.abs_path + '.git'

    @property
    def link(self):
        return SITE_LINK%path.join(self.owner.name, self.name)

    @property
    def clone_addr(self):
        return self.link + '.git'

    @property
    def owner(self):
        return User.get(self.owner_id)

    def clone(self, user):
        clone = Repo()
        clone.owner_id = user.id
        clone.name = '-'.join([self.name, 'forked'])
        clone.desc = self.desc
        check_call(('git clone --bare %s %s'%(self.repo_path, clone.repo_path)).split())
        clone.save()
        return clone

def create_new_repo(user, name, desc):
    new_repo = Repo()
    new_repo.owner_id = user.id
    new_repo.name = name
    new_repo.desc = desc
    check_call(('git init %s --bare'%new_repo.repo_path).split())
    new_repo.save()
    return new_repo

if __name__ == '__main__':
    from user import User
    user = User.where(name='wooparadog')
    if user:
        user = user[0]
        new_repo = create_new_repo(user, 'hello_world', 'null')
        print new_repo.name
        print new_repo.owner.name
        print new_repo.link
        print new_repo.clone(user)
        print new_repo.abs_path
