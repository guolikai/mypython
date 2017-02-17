#!/usr/bin/env python

sum100 = 0
counter = 0

while counter < 100:
    counter += 1
    if not counter % 2:
        continue

    sum100 += counter
else:
    print sum100
