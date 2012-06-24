#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from _base import Model, McModel
from repo import Repo
from subprocess import check_call
import tempfile
import shutil

class PullRequest(McModel):
    @property
    def from_repo(self):
        return Repo.mc_get(self.from_repo_id)

    @property
    def to_repo(self):
        return Repo.mc_get(self.to_repo_id)

    def save_merged(self):
        print "SU!"
        
    def merge(self):
        worktree = tempfile.mkdtemp()
        try:
            check_call(['git', 'clone', '-b', self.to_branch, self.to_repo.repo_path, worktree])

            print ' '.join(['git', '--git-dir', os.path.join(worktree, '.git'),
                        '--work-tree', worktree,
                        'pull', self.from_repo.repo_path, self.from_branch])

            check_call(['git', '--git-dir', os.path.join(worktree, '.git'),
                        '--work-tree', worktree,
                        'pull', self.from_repo.repo_path, self.from_branch])
            check_call(['git', '--git-dir', os.path.join(worktree, '.git'),
                        '--work-tree', worktree,
                        'push', 'origin', self.to_branch])
            self.save_merged()
        finally:
            shutil.rmtree(worktree)

