#!/usr/bin/env python
# coding=utf-8
"""
按定义 - 暴力法
压缩空间 - 多次遍历，多置标志位
O(N)
O(1)
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find n
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next

        times = n // k
        cur = head
        lastTail = None
        newHead = None
        # reverse every k
        for x in range(times):
            first = cur
            pre = None
            tmpCnt = 0
            while tmpCnt < k:
                next = cur.next
                cur.next = pre
                pre, cur = cur, next
                tmpCnt += 1
            if lastTail:
                lastTail.next = pre
            else:
                newHead = pre
            lastTail = first

        # reverse the n%k
        lastTail.next = cur
        return newHead


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve

    # output
    print(time.time() - begin_clock, 'seconds')
