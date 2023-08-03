#!/usr/bin/env python
# coding=utf-8
'''找到最终为0的行与列，将其空间重复利用，作为标志位。
O(m*n + m + n)
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

        srow, scolumn = None, None
        for i in range(l):
            for j in range(w):
                if matrix[i][j] == 0:
                    srow, scolumn = i, j
                    break
            else:
                continue
            break
        else:
            return
        
        for i in range(l):
            for j in range(w):
                if matrix[i][j] == 0:
                    matrix[i][scolumn] = 0
                    matrix[srow][j] = 0
        
        for j in range(w):
            if matrix[srow][j] != 0:
                continue
            if j == scolumn:
                continue
            for i in range(l):
                i == srow
                matrix[i][j] = 0
        
        for i in range(l):
            if matrix[i][scolumn] != 0:
                continue
            if i == srow:
                continue
            for j in range(w):
                matrix[i][j] = 0

        for i in range(l):
            matrix[i][scolumn] = 0
        for j in range(w):
            matrix[srow][j] = 0


if __name__ == '__main__':
    
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    a = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(a)
    print(a)

    # resolve   
    # output
    print(time.time() - begin_clock, 'seconds')
