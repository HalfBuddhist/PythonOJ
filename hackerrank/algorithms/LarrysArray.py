#!/usr/bin/env python
# coding=utf-8
__author__ = 'Qingwei'

def rotate(arr, end):
    maxx = max(arr[end - 1], arr[end - 2], arr[end])
    t = arr[end]
    arr[end] = maxx
    if arr[end - 2] == maxx:
        # rotate_num = 2
        arr[end - 2] = arr[end - 1]
        arr[end - 1] = t
    elif arr[end - 1] == maxx:
        # rotate_num = 1
        arr[end - 1] = arr[end - 2]
        arr[end - 2] = t

def buble_sort_by_three_rotation(arr):
    l = len(arr)
    for times in xrange(l - 2):
        cur_idx = 2
        end_idx = l - 1 - times
        while cur_idx <= end_idx:
            rotate(arr, cur_idx)
            cur_idx += 2 if end_idx - cur_idx >= 2 else 1

t = input()
for t_idx in xrange(t):
    n = input()
    arr = [int(x) for x in raw_input().strip().split()]
    # buble sort them until the last two letter in the left
    buble_sort_by_three_rotation(arr)
    if arr[0] < arr[1]:
        print 'YES'
    else:
        print 'NO'
