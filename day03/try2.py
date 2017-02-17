#!/usr/bin/env python

try:
    num = int(raw_input("number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError), e:
    print "Invalid input:", e
except (KeyboardInterrupt, EOFError):
    print "\nBye-bye"
else:
    print result
finally:
    print 'done.'
