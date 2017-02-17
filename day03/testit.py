#!/usr/bin/env python

import time

start = time.time()
for i in xrange(10000000):
    1282 + 2345
end = time.time()

print end - start

