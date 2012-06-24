#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
from _base import redis
from base64 import b64encode
from config import SESSION_KEY

def randbytes2(bytes):
    return b64encode(os.urandom(bytes)).rstrip('=')

def set_user_session(user):
    random_key = randbytes2(8)
    redis.hset(SESSION_KEY, user.id, random_key)
    return random_key

def verify_user_session_by_user(user, session):
    return session == redis.hget(SESSION_KEY, user.id)

def verify_user_session_by_user_id(user_id, session):
    from user import User
    user = User.mc_get(user_id)
    if user:
        return verify_user_session_by_user(user, session)

