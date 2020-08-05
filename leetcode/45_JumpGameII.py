#!/usr/bin/env python
# coding=utf-8

from sys import maxint
from heapq import *


class Node(object):
    def __init__(self, key):
        self.key = key
        self.cnt = 1
        self.left = None
        self.right = None
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def height(self, node):
        return node.height if node else 0

    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    def put(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self._put(key, self.root)

    def _put(self, key, node):
        if node is None:
            node = Node(key)
        elif key < node.key:
            node.left = self._put(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.key:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)

        elif key > node.key:
            node.right = self._put(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key < node.right.key:
                    node = self.doubleRightRotate(node)
                else:
                    node = self.singleRightRotate(node)
        else:
            node.cnt += 1

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def delete(self, key):
        self.root = self.remove(key, self.root)

    def remove(self, key, node):
        if node is None:
            raise KeyError, 'Error,key not in tree'
        elif key < node.key:
            node.left = self.remove(key, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)

        elif key > node.key:
            node.right = self.remove(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)

        else:  # node to delete
            if node.cnt == 1:
                if node.left and node.right:
                    if node.left.height <= node.right.height:
                        minNode = self._findMin(node.right)
                        node.key = minNode.key  # back up data
                        node.cnt = minNode.cnt
                        minNode.cnt = 1
                        node.right = self.remove(node.key, node.right)
                    else:
                        maxNode = self._findMax(node.left)
                        node.key = maxNode.key
                        node.cnt = maxNode.cnt
                        maxNode.cnt = 1
                        node.left = self.remove(node.key, node.left)
                else:
                    node = node.right if node.right else node.left
            else:
                node.cnt -= 1
        if node:
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node


class IDXJump(object):
    def __init__(self, max_jump_to, least_jump):
        self.max_jump_to = max_jump_to
        self.least_jump = least_jump


class Solution(object):
    def jump_bfs(self, nums):
        """
        BFS in Graph, SPCS;
        Imagine this problem into one graph problem, vertex as the element in the array.
        Edge indicate if the directed jump possibe, and this is the key to sovling the problem.
        Then is a equal-weighted shoteds path problem in the graph. BFS is the solution.
        When doing BFS, no need to form the graph totally, which could incur more complexity.
        Just simulate the traversal process, first level, then the second level, third level....
        level is the step, need an variable to store this info, initialized as 1.
        the queue is not needed, because the order in the queue is the same in the array.
        Increase the step, when step into the next level, that is maximum jump range of the above level
        has come to the end, indicated by variable 'max_range', next_range is to statistic the max jump
        range of the curretn level.
        O(n) in time; O(1) in space; Best performance.
        AC
        :param nums:
        :return:
        """
        n = len(nums)
        if n <= 1:
            return 0
        # maxrange, the max jump for current step.
        step, max_range, next_range = 1, nums[0], nums[0]
        for i in xrange(1, n):
            if max_range >= n - 1:
                return step  # the steps number
            if i > max_range:  # could not jump to i
                max_range = next_range
                step += 1
            next_range = max(next_range, i + nums[i])
        return step

    def jump_dp_iterative(self, nums):
        """
        DP, base algo; bottom-up manner.
        f(i) = min(f(i-x)+1), x: 1 <- i;
        ensure this: i-x+nums[i-x] >= i, that is capability to jump to here.
        The minimum is always needed, so the priority queue is better provied.
        In the iterative process,  the f(x) not meeting the conditons, should be deleted from the priority queue.
        The smallest item always be deleted first, so the priority queue is better to store.
        When they deleted, the corresponding item in the first structure should be deleted as well, but the heap delete process is quite
        complicated, so a balanced searching tree should be exploit instead.
        O(nlogn) in time; O(n) in space.
        AC, but very slow.
        :type nums: list[int]
        :rtype: int
        """
        n = len(nums)
        prior = []
        avl = AVLTree()
        f = []
        for idx in xrange(n):
            f.append(IDXJump(idx + nums[idx], -1))
            while prior and prior[0][0] < idx:
                t = heappop(prior)
                avl.delete(t[1].least_jump)

            f[idx].least_jump = (1 + avl.findMin().key) if avl.root else 0

            # for next
            avl.put(f[idx].least_jump)
            heappush(prior, (f[idx].max_jump_to, f[idx]))

        return f[n - 1].least_jump

    def _dp(self, nums, f, i):
        if f[i] != maxint: return f[i]
        # calc
        minn = maxint - 1  # unreachable
        for pre in xrange(0, i, 1):
            cha = i - pre
            if nums[pre] < cha:
                continue
            else:
                dis = self._dp(nums, f, pre) + 1
                minn = min(dis, minn)

        f[i] = minn
        return minn

    def jump_recursive_dp(self, nums):
        """
        DP, base algo; top-down manner.
        f(i) = min(f(i-x)+1), x: 1 <- i;
        ensure this: i-x+nums[i-x] >= i, that is capability to jump to here.
        top down manner.
        O(n^2)
        Stack overflow.
        :param nums:
        :return:
        """
        n = len(nums)
        f = [maxint for _ in xrange(n)]
        if n > 0: f[0] = 0
        return self._dp(nums, f, n - 1)

    def jump_bf(self, nums):
        """
        Brute force, defination
        enumerate every jump from the beginning, the jump number is the current jump plusing one.
        for every point picking the least jump numbers.
        O(n*max(mi))
        TLE
        :type nums: list[int]
        :rtype: int
        """
        n = len(nums)
        f = [maxint for _ in xrange(n)]
        if n > 0: f[0] = 0
        i = 0
        for x in nums:
            for y in xrange(0, x + 1, 1):
                if i + y < n:
                    f[i + y] = min(f[i + y], 1 + f[i])
                else:
                    break
            i += 1
        return f[n - 1]


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    # try:
    # while True:
    #         n = int(raw_input())
    #         ar = map(int, raw_input().strip().split(' '))
    #         print Solution().jump_bfs(ar)
    # except EOFError as e:
    #     pass

    # ar = map(int, raw_input().split(' '))
    # print ar
    # # print len(ar)
    # # print max(ar)
    # # for x in ar:
    # #     print x,
    # # print
    # print Solution().jump(ar)

    print Solution().jump_bfs([5])

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'