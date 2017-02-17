#!/usr/bin/env python

import time

for i in range(1, 11):
    print i
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print "Bye-bye"
        break
