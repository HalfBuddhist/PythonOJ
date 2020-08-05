#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        idx = []
        cur = head
        while cur is not None:
            idx.append(cur)
            cur = cur.next
        l = len(idx)
        if n == l:
            return head.next
        idx[l - n - 1].next = idx[l - n].next
        return head

    def removeNthFromEnd2(self, head, n):
        """
        2 pointers
        """
        guard = ListNode(-1)
        guard.next = head
        first = guard
        second = guard
        len = 0
        while first.next is not None:
            first = first.next
            if len == n:
                second = second.next
            else:
                len += 1
        # the one after second should be deleted
        second.next = second.next.next
        return guard.next


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input

    # resolve
    # output
    print time.clock() - begin_clock
