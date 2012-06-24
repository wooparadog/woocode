#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from _url import addHandlers  
from _base import baseHandler
from model.repo import Repo, create_new_repo
from model.pull_request import PullRequest, get_pull_request_by_repo
from model.user import User
from config import RESERVED_PATH

def parse_url(username, repo):
    user = User.where(name=username)
    if user:
        user = user[0]
        repo = Repo.where(owner_id=user.id, name=repo)
        if repo:
            repo = repo[0]
            return repo

@addHandlers(r'^/repos/new$')
class New(baseHandler):
    def get(self):
        self.render("/app/repo/new.html")

    def post(self):
        #TODO: hey, add user?!!!
        user = self.get_argument("user", 'wooparadog')
        user = User.get(name=user)
        repo_name = self.get_argument("name", None)
        repo_desc = self.get_argument("desc", None)

        re_dir = create_new_repo(user=user, name=repo_name, desc=repo_desc)
        self.redirect(re_dir.link)


@addHandlers(r'^/((?!%s)[a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)$'%RESERVED_PATH)
class Index(baseHandler):
    def get(self, username, repo):
        repo = parse_url(username, repo)
        if repo:
            return self.render("/app/repo/repo.html", repo=repo)
        raise tornado.web.HTTPError(404)

@addHandlers(r'^/((?!%s)[a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)/fork$'%RESERVED_PATH)
class Fork(baseHandler):
    def post(self, username, repo):
        repo = parse_url(username, repo)
        if repo:
            #TODO: current_user
            fork = repo.clone(repo.owner)
            if fork:
                return self.redirect(fork.link)
        raise tornado.web.HTTPError(404)

@addHandlers(r'^/((?!%s)[a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)/pullrequests/(\d+)$'%RESERVED_PATH)
class PullRequestPage(baseHandler):
    def get(self, username, repo, pullrequest):
        repo = parse_url(username, repo)
        if repo:
            request = PullRequest.mc_get(pullrequest)
            if request:
                return self.render("/app/repo/pullrequest.html", request=request)
            else:
                return self.redirect(repo.link)
        raise tornado.web.HTTPError(404)
        

    def post(self, username, repo, pullrequest):
        repo = parse_url(username, repo)
        if repo:
            request = PullRequest.mc_get(pullrequest)
            if request:
                #TODO: Privileges
                request.merge()
                return self.redirect(request.to_repo.link)
        raise tornado.web.HTTPError(404)

@addHandlers(r'^/((?!%s)[a-zA-Z0-9_]+)/([a-zA-Z0-9_]+)/pullrequest$'%RESERVED_PATH)
class CreatePullRequest(baseHandler):
    def post(self, username, repo):
        repo = parse_url(username, repo)
        if repo:
            pullrequest = repo.create_pull_request(user=self.current_user)
            if pullrequest:
                return self.redirect(pullrequest.link)

        raise tornado.web.HTTPError(404)
