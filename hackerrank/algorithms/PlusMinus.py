#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

a = b = c = 0
for ele in arr:
    if ele > 0:
        a += 1
    elif ele < 0:
        b += 1
    else:
        c += 1

print "%.6f"%(float(a)/n)
print "%.6f"%(float(b)/n)
print "%.6f"%(float(c)/n)

