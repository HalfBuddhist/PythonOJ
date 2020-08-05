#!/usr/bin/env python
# coding=utf-8

class Solution:
    def getWinner(self, arr, k):
        # get max
        max = -1
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]

        if k >= len(arr)-1:
            return max

        a = arr[0]
        b = arr[1:]
        c = []

        cnt = 0
        bindex = 0
        while cnt < k:
            if bindex >= len(b):
                bindex = 0
                b = c
                c = []

            if b[bindex] > a:
                c.append(a)
                a = b[bindex]
                bindex += 1
                cnt = 1
            else:
                cnt += 1
                c.append(b[bindex])
                bindex += 1

        return a


if __name__ == '__main__':
    s = Solution()

    arr = [2, 1, 3, 5, 4, 6, 7]
    k = 2
    print(s.getWinner(arr, k))

    arr = [3, 2, 1]
    k = 10
    # print s.combinationSum(a, b)
    print(s.getWinner(arr, k))

    arr = [1,9,8,2,3,7,6,4,5]
    k = 7
    print(s.getWinner(arr, k))

    arr = [1,11,22,33,44,55,66,77,88,99]
    k = 1000000000
    print(s.getWinner(arr, k))

    arr = [1, 25, 35, 42, 68, 70]
    k = 1
    print(s.getWinner(arr, k))
