#!/usr/bin/env python
# coding=utf-8
'''
方法一：使用标记数组
思路和算法

我们可以用两个标记数组分别记录每一行和每一列是否有零出现。

具体地，我们首先遍历该数组一次，如果某个元素为 0，
那么就将该元素所在的行和列所对应标记数组的位置置为 true。
最后我们再次遍历该数组，用标记数组更新原数组即可。

O(m*n)
O(m+n)
'''

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        h, w = len(matrix), None
        if h <= 0:
            return 
        else:
            w = len(matrix[0])
        
        ridx = [1] * h
        cidx = [1] * w
        for x in range(h):
            for y in range(w):
                if matrix[x][y] == 0:
                    ridx[x] = 0
                    cidx[y] = 0

        for x in range(h):
            for y in range(w):
                if ridx[x] == 0 or cidx[y] == 0:
                    matrix[x][y] = 0


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
