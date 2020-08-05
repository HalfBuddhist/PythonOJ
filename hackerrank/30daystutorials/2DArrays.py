#!/usr/bin/env python
# coding=utf-8
__author__ = 'Qingwei'

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

maxx = -10*7
for row in xrange(0,4):
    for colomn in xrange(4):
        sum_t = arr[row][colomn]+arr[row][colomn+1]+arr[row][colomn+2]+\
            arr[row+2][colomn]+arr[row+2][colomn+1]+arr[row+2][colomn+2]\
            +arr[row+1][colomn+1]
        if sum_t > maxx:
            maxx = sum_t
print maxx
