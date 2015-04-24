# -*- coding:utf-8 -*-
__author__ = 'Christen'

import time
import timeit

# http://en.literateprograms.org/Fibonacci_numbers_(Python)
# http://wenku.baidu.com/view/29496f7e5acfa1c7aa00cc0d.html


def hr(n):
    for i in range(n):
        print "*",
    print


memo = {0: 0, 1: 1}


def fibm(n):
    if not n in memo:
        memo[n] = fibm(n - 1) + fibm(n - 2)
    return memo[n]


def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # http://docs.python.org/2/library/timeit.html

    print "***** fibm *****"
    print timeit.Timer(stmt='fibm(100)', setup="from __main__ import fibm").timeit(1000000)
    print fibm(60)
    print "***** fibi *****"
    print timeit.timeit('fibi(100)', "from __main__ import fibi", number=10000)
    print fibi(100)

    print "***** fib *****"

    hr(20)
    # http://docs.python.org/2/library/time.html
    starttime = time.clock()
    print fib(20)
    endtime = time.clock()
    print (endtime - starttime)
    print timeit.timeit('fib(20)', "from __main__ import fib", number=10)