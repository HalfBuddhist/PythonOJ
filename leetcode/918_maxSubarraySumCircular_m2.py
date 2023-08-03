#!/usr/bin/env python
# coding=utf-8
"""
方法三：单调队列
思路与算法：问题规约 -> 特征性问题（滑窗问题）-> 单调队列

我们可以将数组延长一倍，即对于 i≥n 的元素，令 nums[i]=nums[i−n]。
然后，对于第二种情况，
nums[0:i] 和 nums[j:n] 可以组成成连续的一段：

因此，问题转换为了在一个长度为 2n 的数组上，寻找长度不超过 n 的最大子数组和。

我们令 si 为前缀和，如果不规定子数组的长度，只需找到最大的 si-sj,其中 j<i。
现在，我们只能考虑所有满足 i−n≤j<i 的 j，用单调队列维护该集合。具体的：

1，遍历到 i 时，单调队列头部元素下标若小于 i−n，则出队。
该过程一直进行，直至队列为空或者队头下标大于等于 i−n，保证长度合法性。

2. 取队头元素作为 j，计算 si-sj，并更新答案，因为队列单调递增，队首元素就是最好的元素了。

3. 若队列尾部元素 k 满足 sk ≥ si，则出队，该过程一直进行，直至队列为空或者条件不被满足。
因为 k<i，k 更容易被步骤 1 剔出，并且作为被减项，sk 比 si 更大，更不具有优势。
综上 si 要全面优于 sk。
核心是sk为首的子串小于si为首的子串在后面，所以没有用了，同时也保证了队列的单调性。

O(n)
O(n)

核心：拼接转化，si-sj 变成同质问题，遍历i, 找到最小的 sj 常数时间内，而且要顺序删除窗口外的，
优先队列不行，单调队列最合适，如何保持单调，构造时（如果用排序会打乱窗口），删除比他大的，
因为窗口外要删除，窗口内不如现插入值，如此可成。
"""

import sys
import time
from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        pre, res = nums[0], nums[0]
        q.append((0, pre))  # (j index, sj)
        for i in range(1, 2 * n):
            while len(q) > 0 and q[0][0] < i - n:
                q.popleft()
            pre += nums[i % n] # si
            res = max(res, pre - q[0][1])
            while len(q) > 0 and q[-1][1] >= pre:
                q.pop()
            q.append((i, pre))
        return res


if __name__ == '__main__':
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    nums = [1, 2, -1]
    print(Solution().maxSubarraySumCircular(nums))
    # resolve
    # output
    print(time.time() - begin_clock, 'seconds')
