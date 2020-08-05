#!/usr/bin/env python
# coding=utf-8
import sys, time


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        for a in nums:
            if a != val:
                nums[cnt] = a
                cnt += 1
        return cnt

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input

    # resolve
    # output
    print time.clock() - begin_clock