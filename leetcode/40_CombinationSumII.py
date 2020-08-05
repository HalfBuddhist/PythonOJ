#!/usr/bin/env python
# coding=utf-8

class NumberCnt(object):
    def __init__(self, number, cnt):
        self.number = number
        self.cnt = cnt


class Solution(object):
    def _calc(self, target, csum, path, number_cnt, ans, t_ans):
        if csum == target:
            ans.append(t_ans)
            return
        elif csum > target:
            return
        if path == -1: return

        for x in xrange(number_cnt[path].cnt + 1):
            self._calc(target, csum + x * number_cnt[path].number, path - 1, number_cnt, ans,
                       t_ans + [number_cnt[path].number] * x)

    def combinationSum2(self, candidates, target):
        """
        Base algo, backtracing and recursive
        TIP: statistic and convert the candidates array to accumulate the identic elements into one numbercnt,
        to avoid the repeated occurence. Then use the recursive and backtracking technique to iteratively enable the
        occurense of every numbercnt to search for all the solutions.
        O(2^n) AC; n, length of the candidates array;
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        number_cnt = []
        candidates.sort()
        n = len(candidates)
        cnt = 0
        for i in xrange(n):
            if i == 0: continue
            if candidates[i] == candidates[i - 1]:
                cnt += 1
            else:
                t = NumberCnt(candidates[i - 1], cnt + 1)
                number_cnt.append(t)
                cnt = 0
        number_cnt.append(NumberCnt(candidates[n - 1], cnt + 1))

        self._calc(target, 0, len(number_cnt) - 1, number_cnt, ans, [])
        return ans


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    a = [10, 1, 2, 7, 6, 1, 5]
    b = 8
    print Solution().combinationSum2(a, b)

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'