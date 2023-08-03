#!/usr/bin/env python
# coding=utf-8
"""2 pointer tech
思路：关键是将问题转化成单一数组，之后结合实际场景就想到了双指针技巧，解决。

一般思路：无法分治，动态规划超时，暴力超时，贪心，怎么贪？刚开始就加最多的油，看能不能冲过去，
否则其他开始结点肯定不能冲过去，反证法可以证明。
这样的话就转化成了最大子串和的问题（只不过这里是循环的, 只有退出条件不一样，一个是cur到末尾，
一个是start到末尾），这个问题的典型解法是贪心算法的双指针技巧。

O(n)
O(n)(也可以O(1), 不过每次引用都要减一下。)
"""

import sys, time
from queue import PriorityQueue
from collections import deque


class Solution(object):


    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        h = [0] * n
        for x in range(n):
            h[x] = gas[x] - cost[x]

        start = 0
        while start < n:
            if h[start] >= 0:
                break
            start += 1
        else:
            return -1
        
        end = start
        cur = start + 1
        cur %= n
        summ = h[start]

        while cur != start:
            summ += h[cur]
            if h[cur] < 0:
                if summ < 0:
                    if cur + 1 <= start:
                        return -1
                    start = cur + 1
                    while start < n:
                        if h[start] >= 0:
                            break
                        start += 1
                    else:
                        return -1
                    end = start
                    cur = start + 1
                    summ = h[start]
                else:
                    cur += 1
            else:
                end = cur
                cur += 1
            cur %= n
        
        return start
            

if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(Solution().canCompleteCircuit(gas, cost))
    # resolve   
    # output
    print(time.time() - begin_clock, 'seconds')
