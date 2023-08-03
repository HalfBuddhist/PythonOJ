#!/usr/bin/env python
# coding=utf-8

import sys
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def generateTreesCur(self, start, end):
        if start > end: 
            return [None]

        res_total = []
        for r in range(start, end + 1):
            left = self.generateTreesCur(start, r - 1)
            right = self.generateTreesCur(r + 1, end)
            for l in left:
                for ri in right:
                    node = TreeNode(r, l, ri)
                    res_total.append(node)
        return res_total

    def generateTrees(self, n: int):
        return self.generateTreesCur(1, n)


if __name__ == '__main__':

    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input

    # resolve
    a = Solution().generateTrees(3)
    # output
    print(time.time() - begin_clock, 'seconds')
