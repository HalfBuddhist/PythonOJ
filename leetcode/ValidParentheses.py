#!/usr/bin/env python
# coding=utf-8
import sys, time


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = '([{'
        right = ')]}'
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if len(stack) > 0:
                    top_c = stack.pop()
                    if right.index(c) == left.index(top_c):
                        pass
                    else:
                        return False
                else:
                    return False

            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    sol = Solution()
    s = raw_input().strip()
    try:
        while s is not None and s != '':
            print sol.isValid(s)
            s = raw_input().strip()
    except EOFError as e:
        pass

    # resolve
    # output
    print time.clock() - begin_clock