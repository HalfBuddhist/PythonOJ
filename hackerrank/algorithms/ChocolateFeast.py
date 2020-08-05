#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = map(int, raw_input().strip().split(' '))
    current_wrappers = n/c
    chocolate_cnt = 0
    chocolate_cnt += current_wrappers
    while current_wrappers/m > 0:
        chocolate_cnt += current_wrappers/m
        current_wrappers = (current_wrappers/m + current_wrappers%m)
    print chocolate_cnt
