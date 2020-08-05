#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def longestValidParentheses(self, s):
        """
        DP, Basal algo
        f(i): length of the maxmium parenthese substring end on i.
        = 0 if char = (
        = f(i-1) + 2 + f(i-l); [l = f(i-1) +2 ] if char = ) and found an matched ( before f(i-1)+1 location
        = 0 if no found an matched (
        O(n) time O(n)space
        Ac
        :type s: str
        :rtype: int
        """
        max_len = 0
        n = len(s)
        f = [0] * n
        for i in xrange(n):
            if s[i] == '(':
                f[i] = 0
            else:
                l = (f[i - 1] + 1) if i > 0 else n
                if i > 0 and i >= l and s[i - l] == '(':
                    f[i] = f[i - 1] + 2 + f[i - l - 1] if i - l - 1 >= 0 else f[i - 1] + 2
                else:
                    f[i] = 0
            max_len = max(f[i], max_len)
        return max_len


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    while True:
        try:
            a = raw_input()
            if a is None:
                break
        except EOFError as e:
            print e
            break
        else:
            print Solution().longestValidParentheses(a)

# resolve
# output
print time.clock() - begin_clock