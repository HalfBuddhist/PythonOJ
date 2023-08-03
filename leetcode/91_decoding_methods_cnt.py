#!/usr/bin/env python
# coding=utf-8

import sys, time

class Solution:
    def numDecodingsInFirstN(self, s, table, n):
        if table[n] != -1:
            return table[n]
        
        cur = s[n-1]
        if n == 1:
            if cur == '0':
                table[n] = 0
            else:
                table[n] = 1
            return table[n]

        k = self.numDecodingsInFirstN(s, table, n-2)
        pre = s[n-2]
        if cur == '0':
            if pre == '1' or pre == '2':
                table[n] = k
            else:
                table[n] = 0
        else:
            l = self.numDecodingsInFirstN(s, table, n-1)
            first = l
            if pre == '1':
                second = k
            elif pre == '2':
                if cur < '7':
                    second = k 
                else:
                    second = 0
            else:
                second = 0
            table[n] = first + second
        return table[n]

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        table = [-1] * 105
        table[0] = 1
        return self.numDecodingsInFirstN(s, table, len(s))


if __name__ == '__main__':
    
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    res = Solution().numDecodings('60')
    print(res)
    # resolve
    # output
    print(time.time() - begin_clock, 'seconds')
