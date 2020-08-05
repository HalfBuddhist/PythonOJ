#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    ontimes = 0
    for ele in a:
        if ele <=0: ontimes += 1
    if ontimes >= k:
        print 'NO'
    else:
        print "YES"
