#!/usr/bin/env python
# coding=utf-8
"""
按定义-暴力法
O(M+N)
O(M)
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        # format map
        a = set(jewels)

        # cnt
        for c in stones:
            if c in a:
                res += 1

        return res


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))

    # output
    print(time.time() - begin_clock, 'seconds')
