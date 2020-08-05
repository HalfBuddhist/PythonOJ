#!/usr/bin/env python
# coding=utf-8

# a = map(int,raw_input().strip().split(" "))
# print a

import sys, time

class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        l = len(arr)
        cnt = 0
        for i in range(0, l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    if (abs(arr[i] - arr[j]) <= a and
                        abs(arr[j]-arr[k]) <= b and
                        abs(arr[i] - arr[k]) <= c):
                        cnt += 1
        return cnt

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input

    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    s = Solution()
    # print s.combinationSum(a, b)
    print(s.countGoodTriplets(arr, a, b, c))

    arr = [1, 1, 2, 2, 3]
    a = 0
    b = 0
    c = 1
    print(s.countGoodTriplets(arr, a, b, c))

    # resolve
    # output
    # print time.clock() - begin_clock, 'seconds'