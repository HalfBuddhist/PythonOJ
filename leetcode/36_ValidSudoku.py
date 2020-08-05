#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isValidSudoku(self, board):
        """
        Brute force: defination
        validate the row rule, column rule and box rule respectively.
        AC: O(1)
        :type board: List[List[str]]
        :rtype: bool
        """
        # test row
        count = {}
        for row in board:
            count.clear()
            for ele in row:
                if ele.isdigit():
                    count[ele] = count[ele] + 1 if count.get(ele) else 1
                    if count[ele] > 1:
                        return False

        # test column
        for x in xrange(9):
            count.clear()
            for row in xrange(9):
                ele = board[row][x]
                if ele.isdigit():
                    count[ele] = count[ele] + 1 if count.get(ele) else 1
                    if count[ele] > 1:
                        return False

        # test boxes
        for n in xrange(9):
            count.clear()
            for row in xrange(3):
                for col in xrange(3):
                    ele = board[row + 3 * (n / 3)][col + 3 * (n % 3)]
                    if ele.isdigit():
                        count[ele] = count[ele] + 1 if count.get(ele) else 1
                        if count[ele] > 1:
                            return False
        return True


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    a = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    s = Solution()
    print s.isValidSudoku(a)
    for row in a:
        print row

    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'