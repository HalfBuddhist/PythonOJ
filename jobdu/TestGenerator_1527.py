#!/usr/bin/env python
# coding=utf-8

import random

n = 10000
f = open('test_1527.txt', 'w')
for i in xrange(n):
    k = random.randint(1, 20)
    f.write("%d\n" % k)
    a = []
    for j in xrange(k):
        a.append(random.randint(-20, 20))
    f.write("%s\n" % (' '.join(map(str, a))))

