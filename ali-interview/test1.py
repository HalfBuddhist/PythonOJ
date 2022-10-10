#!/usr/bin/env python
# coding=utf-8
'''常数O(1)时间内删除链表中指定结点
给定链表头指针，待删除结点指针
最后1个分支，复杂度为O(n), 但概率也很小，为1/n, 所以期望复杂度为O(1)
'''

import sys
import time


class Node(object):
    def __init__(self, num):
        self.num = num
        self.next = None


class Solution:
    def deleteNode(self, head, val):
        if head is None or val is None:
            return None
        if val.next is not None:  # 待删除节点不是尾节点
            tmp = val.next
            val.val = tmp.val
            val.next = tmp.next
        elif head == val:  # 待删除节点只有一个节点，此节点为头节点
            head = None
        else:
            cur = head    # 待删除节点为尾节点
            while cur.next != val:
                cur = cur.next
            cur.next = None
        return head


if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('./in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    print('hello1')

    # resolve
    # output
    # print time.clock() - begin_clock, 'seconds'
