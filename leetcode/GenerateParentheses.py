#!/usr/bin/env python
# coding=utf-8
import sys, time


class Solution(object):
    def addRecursive(self, cur_str, steps, left, right, ans):
        if left + right == 2 * steps:
            if left > 0:
                self.addRecursive(cur_str + '(', steps, left - 1, right, ans)
        else:
            if right == 0 and left == 0:
                ans.append(cur_str)
                return

            if right - left > 0:
                if left >= 1:
                    self.addRecursive(cur_str + '(', steps, left - 1, right, ans)
                self.addRecursive(cur_str + ')', steps, left, right - 1, ans)
            else:
                self.addRecursive(cur_str + '(', steps, left - 1, right, ans)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.addRecursive('', n, n, n, ans)
        return ans


if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    print Solution().generateParenthesis(0)


    # resolve
    # output
    print time.clock() - begin_clock