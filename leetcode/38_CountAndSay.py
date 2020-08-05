#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def countAndSay(self, n):
        """
        Base algo, recursive and backtracking.
        could be recode easily use an iterative way, rather than recursive one.
        o(n), AC
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            a = self.countAndSay(n - 1)
            lenn = len(a)
            cnt = 0
            ans = ""
            for i in xrange(lenn):
                if i == 0: continue
                if a[i] == a[i - 1]:
                    cnt += 1
                else:
                    ans += str(cnt + 1) + str(a[i - 1])
                    cnt = 0
            ans += str(cnt + 1) + str(a[lenn - 1])
            return ans


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    s = Solution()
    for x in xrange(6):
        if x == 0: continue
        print s.countAndSay(x)

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'