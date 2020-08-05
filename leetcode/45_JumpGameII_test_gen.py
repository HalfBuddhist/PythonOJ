#!/usr/bin/env python
# coding=utf-8
import random

N = 10
CNT = 100
f = open('test_45_10.txt', 'w')

for times in xrange(CNT):
    case = []
    for x in xrange(N):
        case.append(random.randint(1, 6))
        # write in
    f.write("%d\n" % len(case))
    for ele in case:
        f.write("%d " % ele)
    f.write("\n")

f.close()



