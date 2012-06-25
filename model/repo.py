#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path as path
from subprocess import check_call
from _base import Model, McModel
from cache import redis_cache
from config import REPO_PATHS, SITE_LINK
from user import User
from utils.utils import chdir, mkdtemp
from config.dependencies.PyGIT import Storage

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
    def fork_link(self):
        return path.join(self.link, 'fork')

    @property
    def request_link(self):
        return path.join(self.link, 'pullrequest')

    @property
    def owner(self):
        return User.get(self.owner_id)

    def clone(self, user):
        clone = Repo()
        clone.owner_id = user.id
        clone.name = '_'.join([self.name, 'forked'])
        clone.desc = self.desc
        clone.from_repo_id = self.id
        check_call(('git clone --bare %s %s'%(self.repo_path, clone.repo_path)).split())
        clone.save()
        return clone

    @property
    def _storage(self):
        if not hasattr(self, "_git_storage"):
            self._git_storage = Storage(self.repo_path, logging)
        return self._git_storage 

    @redis_cache("ls_tree:{rev}")
    def ls_tree(self, rev="HEAD"):
        print "not cache"
        return self._storage.ls_all_tree(rev=rev)

    @property
    def from_repo(self):
        return self.from_repo_id and Repo.mc_get(self.from_repo_id)
    
    def create_pull_request(self, user=None, from_branch='master', to_branch='master'):
        #TODO: verify user privileges
        if self.from_repo:
            if not user:
                user = self.owner
            from pull_request import create_new_pull_request
            pull_request = create_new_pull_request(user, 
                    self, self.from_repo, 
                    from_branch=from_branch,
                    to_branch=to_branch)
            return pull_request

def create_new_repo(user, name, desc):
    new_repo = Repo()
    new_repo.owner_id = user.id
    new_repo.name = name
    new_repo.desc = desc
    check_call(('git init %s --bare'%new_repo.repo_path).split())
    with mkdtemp() as temp:
        check_call(['git','clone',new_repo.repo_path, temp])
        with chdir(temp):
            check_call(['touch','README'])
            check_call(['git', 'add', '.'])
            check_call(['git','commit','-m','first commit'])
            check_call(['git','push','origin', 'master'])
    new_repo.save()
    return new_repo

if __name__ == '__main__':
    from user import User, create_new_user 
    try:
        user = create_new_user('wooparadog', 'guohaochuan@gmail.com','123','123')
    except:
        user = User.where(name='wooparadog')
        if user:
            user = user[0]

    try:
        new_repo = create_new_repo(user, 'hello_world', 'null')
    except:
        new_repo = Repo.where(owner_id=user.id, name="hello_world")
        if new_repo:
            new_repo = new_repo[0]
    print "!~"

    print new_repo.name
    print new_repo.owner.name
    print new_repo.link
    #print new_repo.clone(user)
    print new_repo.abs_path
    print new_repo.ls_tree()
