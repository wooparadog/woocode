#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import atexit
import fcntl
from server import main

PID_FILE = 'run.pid'

def _del_pid_file():
    os.remove(PID_FILE)

def single_process():
    # write pid
    pid = os.getpid()
    try:
        pid_fp = os.open(PID_FILE, os.O_WRONLY | os.O_CREAT, 0644)
        fcntl.flock(pid_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.ftruncate(pid_fp, 0)
        os.write(pid_fp, '%s\n' % pid)
    except (IOError, OSError), e:
        sys.stderr.write('pid write error: %s\n' % e)
        sys.exit(1)
    atexit.register(_del_pid_file)

if __name__ == '__main__':
    single_process()
    main()
