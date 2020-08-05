#!/usr/bin/env python
# coding=utf-8
import sys, time
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        O(n^2l), high in time complexity.
        """
        cur = ans = ListNode(-1)
        heads = lists
        l = len(lists)
        while reduce(lambda x, y: x or y is not None, heads, False):
            minv = sys.maxint
            min_idx = 0
            for i in xrange(l):
                if (heads[i] is not None and heads[i].val < minv):
                    minv = heads[i].val
                    min_idx = i
            ans.next = heads[min_idx]
            heads[min_idx] = heads[min_idx].next
            ans = ans.next
        return cur.next


if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    # lists = list(raw_input())
    lists = input()
    print len(lists)
    for listnode in lists:
        for ele in listnode:
            print ele,
        print




    # solution
    # plist = []
    # for ele in lists:
    #     cur = Head = ListNode(-1)
    #     for i in ele:
    #         cur.next = ListNode(i)
    #         cur = cur.next
    #     plist.append(Head.next)
    #
    # Solution().mergeKLists(plist)

    # resolve
    # output
    print time.clock() - begin_clock