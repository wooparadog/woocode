#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _base import Model, McModel

class User(McModel):
    pass

if __name__ == '__main__':
    new_user = User()
    new_user.name="wooparadog"
    new_user.password='111'
    new_user.save()
    

    
