#!/usr/bin/env python
# coding=utf-8
__author__ = 'Qingwei'

p, q = [long(raw_input().strip()) for x in range(2)]
cnt = 0
for a in xrange(p, q + 1, 1):
    square = a ** 2
    d = len(str(a))
    right = square % (10 ** d)
    left = square / (10 ** d)
    if left + right == a:
        cnt += 1
        print a,
if not cnt:
    print 'INVALID RANGE'
else:
    print
