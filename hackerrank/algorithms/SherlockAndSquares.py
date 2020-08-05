#!/usr/bin/env python
# coding=utf-8

import math, sys
from StringIO import StringIO

squares = [0, 1, 4, 9, 16]

def binary_search(target, array, start, end):
    if start > end:
        return -1
    mid_idx = (start + end)/2
    if array[mid_idx] > target:
        return binary_search(target, array, start, mid_idx-1)
    elif array[mid_idx] == target:
        return mid_idx
    else:
        return binary_search(target, array, mid_idx+1, end)

def is_square(test_number):
    #check if expand
    now_square = len(squares) - 1
    should_square = int(math.sqrt(test_number))
    if now_square < should_square:
        for a0 in xrange(now_square+1, should_square+1):
            squares.append(a0*a0)

    #binary search then
    return binary_search(test_number, squares, 0, should_square) != -1

sys.stdin = open('input.txt', 'r')
T = input()
for a0 in xrange(T):
    A, B = map(int, raw_input().strip().split())
    cnt = 0
    for test_num in xrange(A, B+1):
        if is_square(test_num):
            cnt += 1
    print cnt
