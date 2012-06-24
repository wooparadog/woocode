#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import tempfile
from contextlib import contextmanager

@contextmanager
def chdir(dir):
    cwd = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(cwd)

@contextmanager
def mkdtemp():
    tmpdir = tempfile.mkdtemp()
    yield tmpdir
    shutil.rmtree(tmpdir)

