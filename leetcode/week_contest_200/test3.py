#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def minSwaps(self, grid):
        n = len(grid)
        des_rs_dict = {}
        des_rs_dict_d = {}
        des_rs = []
        for x in range(n):
            des_rs.append(-1)

        for i in range(n):
            des_r = 0
            for j in range(n-1, 0, -1):
                if grid[i][j] == 0:
                    des_r += 1
                else:
                    break
            des_rs[i] = n-des_r-1
            des_rs_dict[i] = n-des_r-1
            des_rs_dict_d[n-des_r-1] = i

        # check
        if len(des_rs_dict_d) < n:
            return -1

        # moves
        moves = 0
        for i in range(n-1):
            for j in range(0, n-1-i):
                if (des_rs[j] < des_rs[j+1]):
                    pass
                else:
                    moves += 1
                    t = des_rs[j]
                    des_rs[j] = des_rs[j+1]
                    des_rs[j + 1] = t
        return moves


if __name__ == '__main__':
    s = Solution()

    grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
    print(s.minSwaps(grid))

    # arr = [3, 2, 1]
    # k = 10
    # # print s.combinationSum(a, b)
    # print(s.getWinner(arr, k))
    #
    # arr = [1,9,8,2,3,7,6,4,5]
    # k = 7
    # print(s.getWinner(arr, k))
    #
    # arr = [1,11,22,33,44,55,66,77,88,99]
    # k = 1000000000
    # print(s.getWinner(arr, k))
    #
    # arr = [1, 25, 35, 42, 68, 70]
    # k = 1
    # print(s.getWinner(arr, k))
