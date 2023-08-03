#!/usr/bin/env python
# coding=utf-8
'''固定重复利用第一行第一列的空间，所以先缓存一下，是否为0的状态。
为0自然好说，不为0的直接覆盖的结果不影响（为0了应该覆盖，不为0则保持原样啊），
最后形成的结果这一行一列有一个双关，既表征了自己的最终结果，还表征了这一行一列的是否为0。
O(m*n + m + n)
O(1)

---
方法二：使用两个标记变量
思路和算法

我们可以用矩阵的第一行和第一列代替方法一中的两个标记数组，以达到 O(1) 的额外空间。
但这样会导致原数组的第一行和第一列被修改，无法记录它们是否原本包含 0。
因此我们需要额外使用两个标记变量分别记录第一行和第一列是否原本包含 0。

在实际代码中，我们首先预处理出两个标记变量，接着使用其他行与列去处理第一行与第一列，
然后反过来使用第一行与第一列去更新其他行与列，
最后使用两个标记变量更新第一行与第一列即可。
'''

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0


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
