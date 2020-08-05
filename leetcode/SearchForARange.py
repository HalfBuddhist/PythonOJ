#!/usr/bin/env python
# coding=utf-8
import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        SPCS, binary search
        you could treat the target is target - 0.0000000001, and a negative search return would be the insert location.
        the location should be the left boundary if the target exists.
        Find the right boundary in the same process.
        O(logn), n - length of the nums array.
        AC
        :param nums: int list
        :param target: int
        :return:
        """
        left, right, n = -1, -1, len(nums)
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] >= target:
                high = mid - 1
        if low < n and nums[low] == target:
            left = low
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] <= target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
            right = low - 1
            return [left, right]
        else:
            return [-1, -1]

    def searchRange_lib(self, nums, target):
        """
        use bisection lib to proceeding the binary search process.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return [-1, -1]
        a = bisect.bisect_left(nums, target)
        if a >= n or nums[a] != target:
            return [-1, -1]
        else:
            b = bisect.bisect_right(nums, target)
        return [a, b - 1]


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    nums = input()
    target = input()
    print Solution().searchRange(nums, target)


    # resolve
    # output
    print time.clock() - begin_clock, "seconds"