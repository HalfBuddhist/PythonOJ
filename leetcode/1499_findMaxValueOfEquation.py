#!/usr/bin/env python
# coding=utf-8
"""
思路：特征性问题 -> 滑窗取最值问题 -> 单调队列
O(n)
O(n)
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        maxv = -sys.maxsize - 1
        for idx, p in enumerate(points):
            while len(q) > 0 and (q[0][1][0] < p[0] - k):
                q.popleft()
            if len(q) > 0:
                maxv = max(maxv, abs(p[0] - q[0][1][0]) + p[1] + q[0][1][1])
            while len(q) > 0:
                t = q[-1][1]
                if t[1] + (p[0] - t[0]) < p[1]:
                    q.pop()
                else:
                    break
            q.append((idx, p))
        return maxv


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve
    print(Solution().findMaxValueOfEquation(
        [[0, 0], [3, 0], [9, 2]], 3))
    # output
    print(time.time() - begin_clock, 'seconds')
