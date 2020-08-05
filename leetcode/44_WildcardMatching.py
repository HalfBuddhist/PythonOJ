#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isPrefixMatch(self, fmatch, i, j, s, p, sta):
        """
        match the prefix.
        :param fmatch:
        :param i:
        :param j:
        :param s:
        :param p:
        :return: bool
        """
        # negtive resolve
        if j < 0:
            return i < 0
        elif i < 0:
            if p[j] == '*':
                return self.isPrefixMatch(fmatch, i, j - 1, s, p, sta)
            else:
                return False
        # cache check
        if fmatch[i][j] is not None: return fmatch[i][j]

        # calc
        ans = False
        if p[j] == '?':
            ans = self.isPrefixMatch(fmatch, i - 1, j - 1, s, p, sta)
        elif p[j] == '*':
            for x in xrange(sta[j] - 1, i + 1, 1):
                t = self.isPrefixMatch(fmatch, x, j - 1, s, p, sta)
                if t:
                    ans = True
                    break
                else:
                    continue
            else:
                ans = False
        else:
            if s[i] == p[j]:
                ans = self.isPrefixMatch(fmatch, i - 1, j - 1, s, p, sta)
            else:
                ans = False

        # return
        fmatch[i][j] = ans
        return ans


    def isMatch_dp(self, s, p):
        """
        DP, base algo.
        f(i,j), if first i of s match the first j of p;
        f(i,j) = true if f(i-1, j-1) and s[i] == p[j]
                         or p[j] = '*', one of the s[:x] match p[j-1], x:0<i;
                      else = false.
        O(m*n); m, m length of the strings respectively.
        TLE, and should not, just because this is python.
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        sta = []
        cnt = 0
        for ele in p:
            if ele != '*':
                cnt += 1
            sta.append(cnt)  # to prunning.
        fmatch = [[None for _ in xrange(n)] for _ in xrange(m)]  # record if f(i,j) match
        return self.isPrefixMatch(fmatch, m - 1, n - 1, s, p, sta)

    def isMatch(self, s, p):
        """
        Backtracking, base algo;
        Two pointers for each s and p to indicatet the compare point.
        encounter ? and alpha, compare and do the corresponding return.
        when *, only increase the pattern, and record the current state, the * currently match null string.
        after conflict occure, check if * has been encoutered befer, backtracking and adjust the match string of *.
        re-begine until reach the end of the source string.
        O(m*n)
        AC
        :param s:
        :param p:
        :return:
        """
        m = len(s)
        n = len(p)
        idx_m, idx_n, idx_m_match, idx_n_start = 0, 0, -1, -1
        while idx_m < m:
            if idx_n < n and (p[idx_n] == '?' or p[idx_n] == s[idx_m]):
                idx_m += 1
                idx_n += 1
            elif idx_n < n and p[idx_n] == '*':
                idx_m_match = idx_m
                idx_n_start = idx_n
                idx_n += 1
            elif idx_n_start != -1:
                idx_m_match += 1
                idx_m = idx_m_match
                idx_n = idx_n_start + 1
            else:
                return False

        while idx_n < n and p[idx_n] == '*':
            idx_n += 1

        return idx_n == n


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    s = input()
    p = input()
    print s
    print p
    print len(s)
    print len(p)
    print Solution().isMatch(s, p)

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'