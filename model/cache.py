#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
from _base import redis

def create_key(arg_names, defaults, key, args, kwds):
    args_dict = dict(zip(arg_names[-len(defaults):], defaults)) if defaults else {}
    args_dict.update(kwds)
    return key.format(*args, **args_dict)

def redis_cache(key):
    def _(func):
        arg_names, varargs, varkw, defaults = inspect.getargspec(func)
        def __(*args, **kwds):
            cache_key = create_key(arg_names, defaults, key, args, kwds)
            result = redis.hget('redis_cache', cache_key)
            if not result:
                result = func(*args, **kwds)
                redis.hset('redis_cache', cache_key, result)
            else:
                print 'cached'
            return result
        return __
    return _

@redis_cache("11:{redis}")
def test(id, redis="adsfadsf"):
    pass

if __name__ == '__main__':
    test(1, 'asdf')
