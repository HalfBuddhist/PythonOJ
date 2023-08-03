#!/usr/bin/env python
# coding=utf-8
"""
思路：
智力题 - 规律探索 - 有先手优势的，关键是抓成4个球必胜，如果是5，6，7就可以，8就不可以，
我无论取多少，对方都可以取成4，所以面对8必输，即抓成8必胜，推导出面对12必输，抓成12必胜，
所以规律是面对4的整数倍必输，其余可胜。

进面总结 Nim 规律，先手的人当球为 (k+1) 的整数倍时输，其余胜，后手相反， k 为最多的取球数目。

O(1)
O(1)
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List, Optional


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        return True


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve

    # output
    print(time.time() - begin_clock, 'seconds')
