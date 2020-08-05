#!/usr/bin/env python
# coding=utf-8

import math, sys

def is_square(test_number):
    a = int(math.sqrt(test_number))
    if a*a == test_number:
        return True
    else:
        return False

sys.stdin = open('input.txt', 'r')
T = input()
for a0 in xrange(T):
    A, B = map(int, raw_input().strip().split())
    cnt = 0
    for test_num in xrange(A, B+1):
        if is_square(test_num):
            cnt += 1
    print cnt
