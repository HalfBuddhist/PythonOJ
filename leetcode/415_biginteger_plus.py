#!/usr/bin/env python
# coding=utf-8

import sys, time

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1        
        jin = 0
        res = []
        while i >= 0 or j >=0 or jin > 0:
            sum =  jin
            if i >=0:
                sum += ord(num1[i]) - ord('0') 
            if j >=0:
                sum += ord(num2[j]) - ord('0') 

            if sum >= 10:
                cur = sum - 10
                jin = 1
            else:
                cur = sum
                jin = 0
            res.append(chr(cur+ord('0')))
            i -= 1
            j -= 1
        res.reverse()
        return "".join(res)


if __name__ == '__main__':
    begin_clock = time.time()
    # sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    print(Solution().addStrings("11", "222"))
    # resolve
    # output
    print(time.time() - begin_clock, 'seconds')
