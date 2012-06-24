#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.session import verify_user_session_by_user_id
from config import render, SESSION_KEY
import tornado.web

class baseHandler(tornado.web.RequestHandler):
    render = render
    
    @property
    def current_user(self):
        session = self.get_cookie(SESSION_KEY)
        if session:
            user_id, secret = session.split(":")
            user = verify_user_session_by_user_id(user_id, secret)
            return user
