#!/usr/bin/env python
# coding=utf-8

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    flag = [0]*10
    flag[0] = 2
    flag[1] = 1
    cnt = 0
    for iter_digit in str(n):
        int_digit = int(iter_digit)
        if flag[int_digit] == 0:
            if n%int_digit == 0:
                flag[int_digit] = 1
                cnt += 1
            else:
                flag[int_digit] = 2
        elif flag[int_digit] == 1:
            cnt += 1
        else:
            pass

    print cnt
