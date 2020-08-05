#!/usr/bin/env python
# coding=utf-8
from bisect import bisect_left


class Solution(object):
    def searchInsert(self, nums, target):
        """
        SPCS, binary search
        binar search in the array, the exited low would be the answer to the no-found situation,
        becase [0:low-1], would all less than the target,
        [high+1:n] would be all larger than target, high + 1 = low, so[low:n]
        then the insert point is obvious.
        O(logn)
        AC
        :param nums:
        :param target:
        :return:
        """
        low, high, mid = 0, len(nums) - 1, 0
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return low

    def searchInsert_lib(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect_left(nums, target)


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    print Solution().searchInsert([1], 1)


    # resolve
    # output
    print time.clock() - begin_clock