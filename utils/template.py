#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from config import STATIC_DOMAIN

def static(url):
    return STATIC_DOMAIN%url
