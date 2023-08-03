#!/usr/bin/env python
# coding=utf-8
"""
思路：常数时间内寻找最值 -> 特征性问题 -> 单调队列（常数时间）
全部操作为 O(1), 
如果不要求常数时间，也可以使用优先队列来实现，push 时为 O(logn), 其余常数时间内。
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Node:
    def __init__(self, v):
        self.v = v
        self.next = None


class MaxQueue:

    def __init__(self):
        self.vmap = {}
        self.q = deque()
        self.header = None
        self.tail = None

    def max_value(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        node = Node(value)
        if self.tail:
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.header = self.tail = node
        # update map
        if self.vmap.get(value):
            self.vmap[value] += 1
        else:
            self.vmap[value] = 1
        # update queue
        while len(self.q) > 0 and self.q[-1] <= value:
            self.q.pop()
        self.q.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        node = self.header
        self.header = self.header.next
        if not self.header:
            self.tail = self.header
        # update map
        self.vmap[node.v] -= 1
        # update q
        if node.v == self.q[0] and self.vmap[node.v] == 0:
            self.q.popleft()
        return node.v


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve
    q = MaxQueue()
    q.push_back(94)
    q.push_back(16)
    q.push_back(89)
    print(q.pop_front())
    q.push_back(22)
    print(q.pop_front())
    # output
    print(time.time() - begin_clock, 'seconds')
