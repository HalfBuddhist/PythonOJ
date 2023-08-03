#!/usr/bin/env python
# coding=utf-8
"""
思路：列表翻转 - 按照定义 - 模拟题，暴力法
法一：栈存储再重建
O(N), O(N)

法二：
思路：压缩空间 - 多置标志位 - 从头改造，使用标志位存储改造后的两个链表的头指针，
直到后一个列表为空。
O(N), O(1)
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse1(head):
    stash = []
    cur = head
    while cur:
        stash.append(cur)
        cur = cur.next

    n = len(stash)
    cur = head = stash[n - 1]
    for i in range(n - 2, -1, -1):
        cur.next = stash[i]
        cur = cur.next

    cur.next = None

    return head


def reverse2(head):
    pre = head
    cur = pre.next
    pre.next = None

    while cur:
        next = cur.next
        cur.next = pre
        pre, cur = cur, next

    return pre


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    # resolve

    # output
    print(time.time() - begin_clock, 'seconds')
