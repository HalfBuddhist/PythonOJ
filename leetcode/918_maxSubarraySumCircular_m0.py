#!/usr/bin/env python
# coding=utf-8
"""环形数组的最大和问题
贪心算法的双指针技巧
O(n)
O(1)

失败分析：
不行，跟加油站还不一样，因为要选择环形中最大的，所以在cur遇到start时还要推动 start 继续遍历，
而加油站问题就不用了，而且加油站问题已经保证了那个是惟一最优解了，所以加油站算一个极特殊的例子。
而在继续往前推动start时就不能保证 start 的位置是贪心优化的了，
下面的方法跳过一个正数段一个负数段并不能保证得到最优的解，比如下面的测试用例，
或者要按照以前的贪心的办法来保证的话，即验证贪心的方法cur是否会达到现在的位置，
复杂度就会变成O(n*n).

比如下面的测试用例：
[10, -1,-2, 2, -5, 1, 6]

总结：环形数组的最大和问题不适合纯贪心算法。
"""

import sys
import time
from queue import PriorityQueue
from collections import deque


class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        maxnum = max(nums)
        if maxnum <= 0:
            return maxnum

        start = 0
        while nums[start] <= 0:
            start += 1

        end = start
        maxsum, cursum = nums[start], nums[start]
        cur = start + 1
        cur %= n

        while start < n:
            if cur == start:
                skipPos = False
                skipNeg = False
                # should update the start
                while start < n:
                    if nums[start] < 0:
                        skipPos = True
                    if skipPos and nums[start] > 0:
                        skipNeg = True
                    if skipNeg and skipPos:
                        break
                    cursum -= nums[start]
                    if cursum > maxsum:
                        maxsum = cursum
                    start += 1
                else:
                    return maxsum

            cursum += nums[cur]
            if nums[cur] >= 0:
                if cursum > maxsum:
                    maxsum = cursum
                    end = cur
                cur += 1
            else:
                if cursum < 0:
                    if cur + 1 <= start:
                        return maxsum
                    start = cur + 1
                    while start < n:
                        if nums[start] > 0:
                            break
                        start += 1
                    else:
                        return maxsum
                    cur = start + 1
                    cursum = nums[start]
                    if cursum > maxsum:
                        end = cur
                        maxsum = cursum
                else:
                    cur += 1
            cur %= n

        return maxsum


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # nums =  [1,-2,3,-2]
    # nums =  [-1, -2, -3]
    # nums = [3,-2,2,-3]
    # nums = [5, -3, 5]
    # nums = [0,5,8,-9,9,-7,3,-2]
    # nums = [1,-6,-7,4]
    nums = [10, -1, -2, 2, -5, 1, 6]
    # nums = [52,183,124,154,-170,-191,-240,107,-178,171,75,186,-125,61,-298,284,21,-73,-294,253,146,248,-248,127,26,289,118,-22,-300,26,-116,-113,-44,29,252,-278,47,254,-106,246,-275,42,257,15,96,-298,-69,-104,-239,-95,-4,76,-202,156,-14,-178,188,-84,78,-195,-125,28,109,125,-25,-53,58,287,55,-296,198,281,53,-160,146,298,25,-41,-3,27,-242,169,287,-281,19,91,213,115,211,-218,124,-25,-272,278,296,-177,-166,-192,97,-49,-25,168,-81,6,-94,267,293,146,-1,-258,256,283,-156,197,28,78,267,-151,-230,-66,100,-94,-66,-123,121,-214,-182,187,65,-186,215,273,243,-99,-76,178,59,190,279,300,217,67,-117,170,163,153,-37,-147,-251,296,-176,117,68,258,-159,-300,-36,-91,-60,195,-293,-116,208,175,-100,-97,188,79,-270,80,100,211,112,264,-217,-142,5,105,171,-264,-247,138,275,227,-86,30,-219,153,10,-66,267,22,-56,-70,-234,-66,89,182,110,-146,162,-48,-201,-240,-225,-15,-275,129,-117,28,150,84,-264,249,-85,70,-140,-259,26,162,5,-203,143,184,101,140,207,131,177,274,-178,-79,14,-36,104,52,31,257,273,-52,74,276,104,-133,-255,188,-252,229,200,-74,-39,-250,142,-201,-196,-43,-40,255,-149,-299,-197,-175,-96,-155,-196,-24,12,79,71,-144,-59,-120,227,-256,-163,-297,116,286,-283,-31,-221,-41,121,-170,160,205,8,88,25,-272,-107,292,-180,299,94,-97,-81,-134,37,238]
    print(Solution().maxSubarraySumCircular(nums))

    # resolve
    # output
    print(time.time() - begin_clock, 'seconds')
