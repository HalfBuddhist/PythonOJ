#!/usr/bin/env python
# coding=utf-8
import bisect
import copy


class Solution(object):
    def combinationSumBacktracking(self, candidates, target):
        """
        Base algo, Recursive and Backtracking
        find the possible times to compose the target and iterative try every times number,
        backtrack when having enumberated all candidates or exceed the target or find a solution.
        O(nm) AC;
        n, length of the candidates; m, size of target.
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # find the right bound
        nn = len(candidates)
        candidates.sort()
        sorted_c = candidates
        right_bound = bisect.bisect_right(sorted_c, target)
        right_bound = right_bound if right_bound < nn else nn - 1

        # calc
        ans = []
        self._backtracking(ans, sorted_c, target, right_bound, 0, [])
        return ans


    def _backtracking(self, ans, candidates_s, target, location, tsum, cans):
        # check
        if tsum == target:
            ans.append(cans)
            return
        if tsum > target: return
        if location < 0: return

        cyclee_n = (target - tsum) / candidates_s[location]
        for times in xrange(0, cyclee_n + 1):
            self._backtracking(ans, candidates_s, target, location - 1, tsum + times * candidates_s[location],
                               cans + [candidates_s[location]] * times)

    def _calc(self, f, weights, i, target):
        # end condition
        if f[i][target] is not None: return f[i][target]
        # calc
        ans = []
        cur = target
        cnt = 0
        while cur >= 0:
            res = self._calc(f, weights, i - 1, cur)
            if res:
                for ele in res:
                    ans += [copy.deepcopy(ele) + [weights[i - 1]] * cnt]
            else:
                if not cur:
                    ans += [[weights[i - 1]] * cnt]
            # next
            cur -= weights[i - 1]
            cnt += 1
        f[i][target] = ans
        return ans

    def combinationSum(self, candidates, target):
        """
        Base algo, DP
        f(i,j) number of solutions of the sum to j use first i candidates.
        f(i,j) = sum(f(i-1,j) + f(i-2, j-1*c[i]) + f(i-2, j-2*c[i])+ ..... )
        O(nm) AC;
        n, length of the candidates; m, size of target.
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # find the right bound
        nn = len(candidates)
        candidates.sort()
        sorted_c = candidates
        right_bound = bisect.bisect_right(sorted_c, target)
        right_bound = right_bound if right_bound < nn else nn - 1

        # intial
        n = right_bound + 5
        m = target + 5
        f = [[None for column in xrange(m)] for row in xrange(n)]  # n rows and m columns, ele is []
        for x in xrange(m):
            f[0][x] = []
        for x in xrange(n):
            f[x][0] = []

        # calc
        self._calc(f, sorted_c, right_bound + 1, target)

        # return
        return f[right_bound + 1][target]


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input

    a = [8, 7, 4, 3]
    b = 11
    s = Solution()
    # print s.combinationSum(a, b)
    print s.combinationSumBacktracking(a, b)

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'