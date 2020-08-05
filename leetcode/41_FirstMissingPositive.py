#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        Imagination; visualization the situation in your mind.
        Put each number in its right place.
        At last, the first place where its number is not right, return the place + 1.
        O(n); AC
        :type nums: list[int]
        :rtype: int
        """
        n = len(nums)
        for idx in xrange(n):
            ele = nums[idx]
            while 0 < ele <= n and ele != nums[ele - 1]:
                t = nums[ele - 1]
                nums[ele - 1] = ele
                nums[idx] = t
                ele = nums[idx]

        for idx in xrange(n):
            if idx + 1 != nums[idx]:
                return idx + 1

        return 1 + n


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    print Solution().firstMissingPositive([3, 4,-1,1])

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'