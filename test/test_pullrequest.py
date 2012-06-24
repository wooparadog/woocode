#!/usr/bin/env python
# -*- coding: utf-8 -*-
import _env
import unittest
from subprocess import check_call
from model.user import User, create_new_user
from model.repo import Repo, create_new_repo
from model.pull_request import PullRequest
import random
from os.path import join
from utils.utils import chdir, mkdtemp

class TestPullRequest(unittest.TestCase):
    def setup_user(self):
        user_name = 'test%s'%random.randint(0, 100)
        user = create_new_user(user_name, '%s@test.com'%user_name, 'test1', 'test1')
        return user

    def setup_repo(self):
        user = self.setup_user()
        repo_name = 'repo%s'%random.randint(0, 100)
        repo = create_new_repo(user, repo_name, 'foobar')
        return repo

    def setup_clone(self, repo):
        user = self.setup_user()
        return repo.clone(user)

    def test_merge_pull_request(self):
        repo1 = self.setup_repo()
        repo2 = self.setup_clone(repo1)
        content = "this is s a dsafsdf"

        pull_request = PullRequest()
        pull_request.from_repo_id = repo2.id
        pull_request.from_branch = 'master'
        pull_request.to_repo_id = repo1.id
        pull_request.to_branch = 'master'
        pull_request.user_id = repo2.owner_id

        with mkdtemp() as work_path:
            with chdir(work_path):
                check_call(('git clone %s %s'%(repo1.clone_addr, work_path)).split())
                with open(join(work_path, 'orig'), 'w') as f:
                    f.write(content)
                check_call('git add .'.split())
                check_call('git commit -m"f"  -a'.split())
                check_call('git push origin master'.split())

        with mkdtemp() as work_path:
            with chdir(work_path):
                check_call(('git clone %s %s'%(repo2.clone_addr, work_path)).split())
                with open(join(work_path, 'new_file'), 'w') as f:
                    f.write(content)
                check_call('git add .'.split())
                check_call('git commit -m"f"  -a'.split())
                check_call('git push origin master'.split())

        pull_request.merge()

        with mkdtemp() as work_path:
            with chdir(work_path):
                check_call(('git clone %s %s'%(repo1.clone_addr, work_path)).split())
                with open("new_file") as f:
                    self.assertEqual(f.read(), content)

if __name__ == '__main__':
    unittest.main()

