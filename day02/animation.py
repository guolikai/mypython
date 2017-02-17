#!/usr/bin/env python

import time
import sys

for i in range(10):
    for ch in '-/|\\':
        sys.stdout.write("waiting... %s\r" % ch)
        sys.stdout.flush()
        time.sleep(0.2)
