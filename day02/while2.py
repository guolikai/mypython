#!/usr/bin/env python

# yn = raw_input("Continue(y/n)? ")
#
# while yn != 'n':
#     print "working..."
#     yn = raw_input("Continue(y/n)? ")

while True:
    print "working..."
    yn = raw_input("Continue(y/n)? ")
    if yn in 'nN':
        break

print 'done'
