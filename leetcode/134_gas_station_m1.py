#!/usr/bin/env python
# coding=utf-8
"""Brute force
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
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        candi = set()
        for s in range(n):
            if gas[s] >= cost[s]:
                candi.add(s)
            
        for s in candi:
            cgas = 0
            for k in range(n):
                cgas += gas[(s+k)%n]
                cgas -= cost[(s+k)%n]
                if cgas < 0:
                    break
            else:
                return s
            continue      


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    gas = [2,3,4]
    cost = [3,4,3]
    print(Solution().canCompleteCircuit(gas, cost))
    # resolve   
    # output
    print(time.time() - begin_clock, 'seconds')
