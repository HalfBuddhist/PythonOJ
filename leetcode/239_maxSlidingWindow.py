#!/usr/bin/env python
# coding=utf-8
"""
思路：滑窗内寻找最值 -> 特征性问题 -> 单调队列/MAXQUEUE/PQ/SEGMENT TREE

单调队列：O(n), O(k)
MAXQUEUE：上述超集，同上。
PQ: O(nlogn), O(n)
SEGMENT TREE: 忘记，暂时省略。
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for idx, num in enumerate(nums):
            while len(q) > 0 and idx - q[0][0] > k - 1:
                q.popleft()
            while len(q) > 0 and num >= q[-1][1]:
                q.pop()
            q.append((idx, num))
            if idx >= k - 1:
                result.append(q[0][1])
        return result


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve
    a = [1, 3, -1, -3, 5, 3, 6, 7]
    print(Solution().maxSlidingWindow(a, 3))

    # output
    print(time.time() - begin_clock, 'seconds')
