#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def _fill_set(self, board, row_filled, col_filled, box_filled, cur_path):
        """
        fill recursively
        :param board:
        :param row_filled:
        :param col_filled:
        :param box_filled:
        :param cur_path:
        :return: fill succesfull or not
        """
        if cur_path > 80: return True
        crow = cur_path / 9
        ccol = cur_path % 9
        if board[crow][ccol].isdigit():
            return self._fill_set(board, row_filled, col_filled, box_filled, cur_path + 1)
        else:
            # enumerate every possible elements
            for xx in xrange(1, 10):
                x = str(xx)
                if x in row_filled[crow] or x in col_filled[ccol] or x in box_filled[(crow / 3) * 3 + (ccol / 3)]:
                    continue
                else:
                    # possible value
                    board[crow][ccol] = x
                    row_filled[crow].add(x)
                    col_filled[ccol].add(x)
                    box_filled[(crow / 3) * 3 + (ccol / 3)].add(x)
                    if self._fill_set(board, row_filled, col_filled, box_filled, cur_path + 1):
                        return True
                    else:  # recover
                        board[crow][ccol] = '.'
                        row_filled[crow].remove(x)
                        col_filled[ccol].remove(x)
                        box_filled[(crow / 3) * 3 + (ccol / 3)].remove(x)
                        continue
            else:  # no solution found
                return False


    def solveSudokuWithSet(self, board):
        """
        SPCS, DFS or Base algo, recursive and backtracking.
        O(9^n), n - length of the unfilled sudoku cells.
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # get new board
        new_board = [[col for col in row] for row in board]
        # statistic the board
        row_filled = [set() for _ in xrange(9)]
        col_filled = [set() for _ in xrange(9)]
        box_filled = [set() for _ in xrange(9)]
        for row in xrange(9):
            for col in xrange(9):
                if board[row][col].isdigit():
                    row_filled[row].add(board[row][col])
                    col_filled[col].add(board[row][col])
                    box_filled[(row / 3) * 3 + (col / 3)].add(board[row][col])

        # fill
        self._fill_set(new_board, row_filled, col_filled, box_filled, 0)

        # transfer back
        for x in xrange(9):
            a = ""
            for col in xrange(9):
                a += new_board[x][col]
            board[x] = a

    def _fill(self, board, row_filled, col_filled, box_filled, cur_path):
        """
        fill recursively
        :param board:
        :param row_filled:
        :param col_filled:
        :param box_filled:
        :param cur_path:
        :return: fill succesfull or not
        """
        if cur_path > 80: return True
        crow = cur_path / 9
        ccol = cur_path % 9
        if board[crow][ccol].isdigit():
            return self._fill(board, row_filled, col_filled, box_filled, cur_path + 1)
        else:
            # enumerate every possible elements
            for xx in xrange(1, 10):
                x = str(xx)
                if x in row_filled[crow] or x in col_filled[ccol] or x in box_filled[(crow / 3) * 3 + (ccol / 3)]:
                    continue
                else:
                    # possible value
                    board[crow][ccol] = x
                    row_filled[crow].append(x)
                    col_filled[ccol].append(x)
                    box_filled[(crow / 3) * 3 + (ccol / 3)].append(x)
                    if self._fill(board, row_filled, col_filled, box_filled, cur_path + 1):
                        return True
                    else:  # recover
                        board[crow][ccol] = '.'
                        row_filled[crow].remove(x)
                        col_filled[ccol].remove(x)
                        box_filled[(crow / 3) * 3 + (ccol / 3)].remove(x)
                        continue
            else:  # no solution found
                return False


    def solveSudoku(self, board):
        """
        SPCS, DFS or Base algo, recursive and backtracking.
        fill the empty cells with the legal strings iteratively and backtracking when there is no
        possible numbers to fill in the current location.
        O(9^n), n - length of the unfilled sudoku cells.
        AC
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # get new board
        new_board = [[col for col in row] for row in board]
        # statistic the board
        row_filled = [[] for _ in xrange(9)]
        col_filled = [[] for _ in xrange(9)]
        box_filled = [[] for _ in xrange(9)]
        for row in xrange(9):
            for col in xrange(9):
                if board[row][col].isdigit():
                    row_filled[row].append(board[row][col])
                    col_filled[col].append(board[row][col])
                    box_filled[(row / 3) * 3 + (col / 3)].append(board[row][col])

        # fill
        self._fill(new_board, row_filled, col_filled, box_filled, 0)

        # transfer back
        for x in xrange(9):
            a = ""
            for col in xrange(9):
                a += new_board[x][col]
            board[x] = a


import sys, time

if __name__ == '__main__':
    begin_clock = time.clock()
    sys.stdin = open('../in.txt', 'r')
    # sys.stdout = open('out.txt', 'w')
    # presolve
    # input
    a = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
         "...2759.."]
    for x in a:
        print x
    print('\n')
    Solution().solveSudokuWithSet(a)
    for x in a:
        print x
    # resolve
    # output
    print time.clock() - begin_clock, 'seconds'