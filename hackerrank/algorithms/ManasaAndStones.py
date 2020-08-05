#!/usr/bin/env python
# coding=utf-8

t = int(raw_input().strip())

for a0 in xrange(t):
    n = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())
    if a == b :
        print a*(n-1)
    else:
        t = max(a,b); t1 = min(a,b)
        for b0 in xrange(n):
            print (b0*t)+(n-1-b0)*t1,
        print
