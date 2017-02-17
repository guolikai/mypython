#!/usr/bin/env python

fib = [0, 1]

num = int(raw_input("number: "))

for i in range(num - 2):
    fib.append(fib[-1] + fib[-2])

print fib
