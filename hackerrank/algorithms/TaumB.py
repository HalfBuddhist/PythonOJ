#!/usr/bin/env python
# coding=utf-8

import math

t = int(raw_input().strip())
for a0 in xrange(t):
    b, w = map(long, raw_input().strip().split(' '))
    x, y, z = map(long, raw_input().strip().split(' '))
    if math.fabs(x - y) < z:
        print b * x + w * y
    else:
        print b * x + w * (x + z) if x < y else b * (y + z) + w * y