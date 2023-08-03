#!/usr/bin/env python
# coding=utf-8
'''找到一个与矩阵内都不同的数，先置为这个数，然后置其为0。
O(m*m*n*n + m*n*(m+n) + m*n)
O(1)
'''

import sys, time
from queue import PriorityQueue
from collections import deque

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l == 0:
            return 
        w = len(matrix[0])

        target_flag = None
        for n in range(l*w+5, 0, -1):
            for i in range(l):
                for j in range(w):
                    if matrix[i][j] == n:
                        break
                else:
                    continue
                break
            else:
                target_flag = n
                break
            continue

        for i in range(l):
            for j in range(w):
                if matrix[i][j] != 0:
                    continue
                # change i, j
                for k in range(w):
                    if matrix[i][k] != 0:
                        matrix[i][k] = target_flag
                for m in range(l):
                    if matrix[m][j] != 0:
                        matrix[m][j] = target_flag

        for i in range(l):
            for j in range(w):
                if matrix[i][j] == target_flag:
                    matrix[i][j] = 0
        return                   


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    a = [[-1],[2],[3]]
    Solution().setZeroes(a)
    print(a)

    # resolve   
    # output
    print(time.time() - begin_clock, 'seconds')
