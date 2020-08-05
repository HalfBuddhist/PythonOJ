#!/usr/bin/env python
# coding=utf-8

import math, sys

sys.stdin = open('input.txt', 'r')
T = input()
for a0 in xrange(T):
    A, B = map(int, raw_input().strip().split())
    cnt = 0
    sqrt = math.ceil(math.sqrt(A))
    while sqrt*sqrt<=B:
        sqrt += 1
        cnt += 1
    print cnt
