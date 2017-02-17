#!/usr/bin/env python

def gen_fib(num):
    fib = [0, 1]

    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

a = gen_fib(10)
print a
print gen_fib(20)
