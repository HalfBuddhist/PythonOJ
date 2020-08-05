#!/usr/bin/env python
# coding=utf-8
import sys, time


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, cnt = 0, 0
        for num in nums:
            if cnt == 0 or last != num:
                last = num
                nums[cnt] = num
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