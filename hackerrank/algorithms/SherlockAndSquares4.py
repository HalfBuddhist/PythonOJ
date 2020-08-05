#!/usr/bin/env python
# coding=utf-8

import math, sys

sys.stdin = open('input.txt', 'r')
T = input()
for a0 in xrange(T):
    A, B = map(int, raw_input().strip().split())
    print int(math.floor(math.sqrt(B)) - math.ceil(math.sqrt(A)) + 1 + 0.5)
