#!/bin/python

import sys

#m1 map array
a = [0, 3, 1, 4, 2]

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    Nm = n/3
    R = n-3*Nm
    m1 = R%5
    theta = a[m1]
    M = 3*theta

    N5 = 3*Nm-M
    N3 = R+M

    if N5 >= 0:
        print "%s%s"%('5'*N5, '3'*N3)
    else:
        print '-1'
