#!/usr/bin/env python
# -*- coding: utf-8 -*-

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_MAIN = 'woocode'
MYSQL_USER = 'woocode'
MYSQL_PASSWD = 'everythingforyou'

CONNECTION_STRING = '%s:%s:%s:%s:%s' % (
        MYSQL_HOST, MYSQL_PORT, MYSQL_MAIN, MYSQL_USER, MYSQL_PASSWD
    )
