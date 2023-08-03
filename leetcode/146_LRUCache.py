#!/usr/bin/env python
# coding=utf-8
"""
常数时间内最值 - 单调队列 - 特征性问题
O(n)
O(k)
"""


import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.idx = {}

    def get(self, key: int) -> int:
        if key not in self.idx:
            return -1
        else:
            eNode = self.idx[key]
            # move to tail
            pre = eNode.pre
            next = eNode.next
            if next:
                next.pre = pre
            else:
                return eNode.value
            if pre:
                pre.next = next
            else:
                self.head = next
            # put tail
            eNode.next = None
            eNode.pre = self.tail
            self.tail.next = eNode
            self.tail = self.tail.next

            return eNode.value

    def put(self, key: int, value: int) -> None:
        if key in self.idx:
            eNode = self.idx[key]
            eNode.value = value
            # connect pre and next
            pre = eNode.pre
            next = eNode.next
            if next:
                next.pre = pre
            else:
                return
            if pre:
                pre.next = next
            else:
                self.head = next
            # put tail
            eNode.next = None
            eNode.pre = self.tail
            self.tail.next = eNode
            self.tail = self.tail.next
        else:
            node = Node(key, value)
            self.idx[key] = node
            # put to tail
            if not self.tail:
                self.head = self.tail = node
            else:
                node.next = None
                node.pre = self.tail
                self.tail.next = node
                self.tail = self.tail.next
            # remove the lease use
            if len(self.idx) > self.capacity:
                dKey = self.head.key
                self.head = self.head.next
                self.head.pre = None
                self.idx.pop(dKey)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve
    l = LRUCache(3)
    l.put(1, 1)
    l.put(2, 2)
    l.put(3, 3)
    l.put(4, 4)
    print(l.get(4))
    print(l.get(3))
    print(l.get(2))
    print(l.get(1))
    l.put(5, 5)
    print(l.get(1))

    print(l.get(2))
    print(l.get(3))
    print(l.get(4))
    print(l.get(5))
    # output
    print(time.time() - begin_clock, 'seconds')
