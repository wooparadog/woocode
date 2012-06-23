#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from config import DATABASE_CONFIG
from sqlbean.db.sqlstore import SqlStore
from sqlbean.db.mc_connection import init_mc

init_mc(disable_local_cached=True,memcached_addr=("127.0.0.1:11211",))

SQLSTORE = SqlStore(db_config=DATABASE_CONFIG, **{})

def get_db_by_table(table_name):
    return SQLSTORE.get_db_by_table(table_name)

from sqlbean.db import connection

connection.get_db_by_table = get_db_by_table

from sqlbean.shortcut import Model,McModel
