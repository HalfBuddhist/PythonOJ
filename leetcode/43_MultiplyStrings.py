#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    def add(self, num1, num2):
        """
        add two strings
        :param num1: str
        :param num2: str
        :return:
        """
        ans = ""
        i = m = len(num1)
        j = n = len(num2)
        i -= 1
        j -= 1
        jin = 0
        while i >= 0 or j >= 0:
            t = (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0 ) + jin
            ans += str(t % 10)
            jin = t / 10
            # for next
            i -= 1
            j -= 1
        if jin > 0:
            ans += '1'
        return ans[::-1]

    def multiply(self, num1, num2):
        """
        Bruet force, simulate problem
        simulate the muliply process in hand.
        O(m*n), m and n, the length of the strings.
        AC
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = "0"
        m = len(num1)
        n = len(num2)
        for x in xrange(n):
            if num2[x] == '0': continue
            jin = 0
            t = ""
            for y in xrange(m - 1, -1, -1):
                mul = int(num1[y]) * int(num2[x]) + jin
                jin = mul / 10
                t += str(mul % 10)
            if jin > 0:
                t += str(jin)
            #accumulate
            t = t[::-1]
            if not t=='0':
                t += '0' * (n - 1 - x)
            ans = self.add(ans, t)
        return ans


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    print Solution().multiply("100", "100")

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'