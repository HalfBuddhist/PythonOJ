#!/usr/bin/env python
# coding=utf-8
'''
O(m*n + m)
O(1)

方法三：使用一个标记变量
思路和算法

我们可以对方法二进一步优化，只使用一个标记变量记录第一列是否原本存在 0。
这样，第一列的第一个元素即可以标记第一行是否出现 0。
但为了防止每一列的第一个元素被提前更新，我们需要从最后一行开始，倒序地处理矩阵元素。
'''

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(a)
    print(a)

    # resolve
    # output
    print(time.time() - begin_clock, 'seconds')
