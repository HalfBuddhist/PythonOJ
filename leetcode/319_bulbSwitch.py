#!/usr/bin/env python
# coding=utf-8
"""
思路：智力题 - 规律探索 - 数的因子数为奇则开，偶为关 - 素数肯定偶，合数未必，放弃
以平方根为界，至少2个因子1与其本身，还有1到平方根中间还有，则一定还有另外一个因子在平方根到N之间，
也就是说因子是成对出现的，一般为偶，平方数为奇 - 规约成有多少个平方数 - 
即为n的平方根的向下取整即为答案。

O(1)
O(1)
"""


import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List, Optional
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        k = math.sqrt(n)
        return int(k)


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve

    # output
    print(time.time() - begin_clock, 'seconds')
