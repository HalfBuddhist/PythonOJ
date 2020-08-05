#!/usr/bin/env python
# coding=utf-8

class HeightNumber(object):
    def __init__(self, height, number):
        self.height = height
        self.number = number


class Solution(object):
    def trap(self, height):
        """
        SPCS, monotone [priority] queue
        keep the current scanned height a descending monotone queue,
        for the current height, accumulate the trapping water with each height in the queue to the total water trapping.
        enqueue the current height, iteratively solving the problem.
        O(n), length of the height array.
        AC
        :type height: list[int]
        :rtype: int
        """
        mq = []
        n = len(height)
        ans = 0
        for idx in xrange(n):
            ele = height[idx]
            # calc
            nn = len(mq)
            last_h = 0
            last_idx = -1  # indicate the element's height > current height
            for x in xrange(nn - 1, -1, -1):
                # ans += (idx - mq[x].number - 1) * abs(mq[x].height - last_h)
                if mq[x].height <= ele:
                    ans += (idx - mq[x].number - 1) * (mq[x].height - last_h)
                    last_h = mq[x].height
                else:
                    ans += (idx - mq[x].number - 1) * (ele - last_h)
                    last_h = ele
                    last_idx = x
                    break
            else:  # this is the tallest
                last_idx = -1

            # keep a monotone descending queue
            mq = mq[:last_idx + 1]
            mq.append(HeightNumber(ele, idx))
        return ans


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'