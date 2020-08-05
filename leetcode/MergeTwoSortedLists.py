#!/usr/bin/env python
# coding=utf-8
import sys, time
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(-1)
        cur = ans
        end, start = l2, l1
        while start is not None or end is not None:
            if end is None or (start is not None and end is not None and start.val < end.val):
                cur.next = start
                start = start.next
            else:
                cur.next = end
                end = end.next
            cur = cur.next
        return ans.next


if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input

    # resolve
    # output
    print time.clock() - begin_clock