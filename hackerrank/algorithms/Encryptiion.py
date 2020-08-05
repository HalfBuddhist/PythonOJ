#!/usr/bin/env python
# coding=utf-8
__author__ = 'Qingwei'

import math
source = raw_input().strip()
l = len(source)
column = int(math.ceil(math.sqrt(l)))
words = []
for col in xrange(column):
    a = ''
    start = col
    while start<l:
        a += source[start]
        start += column
    words.append(a)
print ' '.join(words)
