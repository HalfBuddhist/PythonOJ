#!/usr/bin/env python
# coding=utf-8

import sys
import time


class Solution(object):

    def minDistanceRoutine(self, table, lword, sword, l, m):
        if m == 0 or l == 0:
            table[l][m] = max(l, m)
            return table[l][m]

        if table[l][m] != -1:
            return table[l][m]

        if lword[len(lword) - l] == sword[len(sword) - m]:
            op1 = self.minDistanceRoutine(table, lword, sword, l - 1, m - 1)
            op2 = 1 + self.minDistanceRoutine(table, lword, sword, l - 1, m)
            table[l][m] = min(op1, op2)
        else:
            op1 = self.minDistanceRoutine(table, lword, sword, l - 1, m - 1) + 1
            op2 = self.minDistanceRoutine(table, lword, sword, l - 1, m) + 1
            op3 = self.minDistanceRoutine(table, lword, sword, l, m-1) + 1
            table[l][m] = min(op1, op2, op3)

        return table[l][m]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        table = [[-1] * (len(word2) + 5) for x in range(len(word1) + 5)]

        self.minDistanceRoutine(table, word1, word2, len(word1), len(word2))
        return table[len(word1)][len(word2)]


if __name__ == '__main__':

    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    print(Solution().minDistance("teacher", "tenace"))
    # resolve
    # output
    print(time.time() - begin_clock, 'seconds')
