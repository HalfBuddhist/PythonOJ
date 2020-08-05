#!/usr/bin/env python
# coding=utf-8
"""
整个过程模拟了从有序到无序的贿赂过程，由于大部分的只翻转2次，而多次的检测到就退出，
所以复杂度为O(n)
没有用到排序的过程，没有反着来思考。
"""

import sys
# sys.stdin=open("in","r")

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    org = [i for i in range(n + 1)]  # 当前的序列，同样类似于一个排序的过程，动态记录
    pos = [i for i in range(n + 1)]  # 元素的当前位置，类似于一个排序的过程，动态记录，相当于一个索引
    cnt = [0 for i in range(n + 1)]  # 逆序数

    ans = 0 # 逆序和
    invalid = 0  # flag if > 2
    for i in range(n - 1, -1, -1): #逆着顺序来处理，先处理最后一个，即在原序列中先将它移到队尾。
        if invalid:
            break
        oldp = pos[arr[i]]
        newp = i + 1  # new posion， 当前位置
        while oldp != newp:
            ans = ans + 1
            cnt[org[oldp + 1]] += 1
            if cnt[org[oldp + 1]] > 2:
                invalid = 1
                break
            org[oldp], org[oldp + 1] = org[oldp + 1], org[oldp]
            pos[org[oldp]] = oldp
            pos[org[oldp + 1]] = oldp + 1
            oldp = oldp + 1

    # print cnt
    if invalid:
        ans = "Too chaotic"
    print ans
