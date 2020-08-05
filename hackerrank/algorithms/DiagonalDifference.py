#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

sum1 = 0
sum2 = 0
for a_i in xrange(n):
    sum1 += a[a_i][a_i]
    sum2 += a[a_i][n-a_i-1]

print abs(sum1-sum2)

