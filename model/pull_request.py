#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from _base import Model, McModel
from repo import Repo
from subprocess import check_call, Popen, PIPE
import tempfile
import shutil

STATUS_CONFILCT = 'C'
STATUS_MERGED = 'M'
STATUS_INIT = 'I'

class PullRequest(McModel):
    @property
    def link(self):
        return os.path.join(self.to_repo.link, 'pullrequests', str(self.id))

    @property
    def creator(self):
        from user import User
        return User.mc_get(self.user_id)

    @property
    def from_repo(self):
        return Repo.mc_get(self.from_repo_id)

    @property
    def to_repo(self):
        return Repo.mc_get(self.to_repo_id)

    def save_merged(self):
        self.status = STATUS_MERGED

    def merge(self):
        worktree = tempfile.mkdtemp()
        try:
            check_call(['git', 'clone', '-b', self.to_branch, self.to_repo.repo_path, worktree])
            check_call(['git', '--git-dir', os.path.join(worktree, '.git'),
                        '--work-tree', worktree,
                        'pull', self.from_repo.repo_path, self.from_branch])
            check_call(['git', '--git-dir', os.path.join(worktree, '.git'),
                        '--work-tree', worktree,
                        'push', 'origin', self.to_branch])
            self.save_merged()
        finally:
            shutil.rmtree(worktree)

    def diff(self):
        worktree = tempfile.mkdtemp()
        try:
            check_call(['git', 'clone', '-b', self.to_branch, self.to_repo.repo_path, worktree])
            check_call(['git', '--git-dir', os.path.join(worktree, '.git'),
                        '--work-tree', worktree,
                        'fetch', self.from_repo.repo_path, self.from_branch])
            diff = Popen(['git', '--git-dir', os.path.join(worktree, '.git'),
                        '--work-tree', worktree,
                        'diff', 'FETCH_HEAD', self.to_branch], stdout=PIPE)
            diff = diff.stdout.read()
            self.save_merged()
            return diff
        except Exception:
            self.status = STATUS_CONFILCT
        finally:
            shutil.rmtree(worktree)



def create_new_pull_request(user, from_repo, to_repo, from_branch='master', to_branch='master'):
    pull_request = PullRequest()
    pull_request.from_repo_id = from_repo.id
    pull_request.from_branch = from_branch
    pull_request.to_repo_id = to_repo.id
    pull_request.to_branch = to_branch
    pull_request.user_id = user.id
    pull_request.status = STATUS_INIT
    pull_request.save()
    return pull_request

def get_pull_request_by_repo(repo):
    pull_request = PullRequest.where(from_repo_id=repo.id)
    if pull_request:
        return pull_request[0]

