#!/usr/bin/env python
# coding=utf-8

import sys

# # metod1 brute force
# sys.stdin = open('input05.txt', 'r')
# t = int(raw_input().strip())
# for a0 in xrange(t):
# R, C = map(int, raw_input().strip().split(' '))
#     G = []
#     for G_i in xrange(R):
#         G_t = str(raw_input().strip())
#         G.append(G_t)
#     r, c = map(int, raw_input().strip().split(' '))
#     P = []
#     for P_i in xrange(r):
#         P_t = str(raw_input().strip())
#         P.append(P_t)
#
#
#     # find pattern
#     if r > R or c > C:
#         print 'NO'
#     else:
#         is_find = False
#         for row in xrange(R - r + 1):
#             for column in xrange(C - c + 1):
#                 t_find = True
#                 for a in xrange(r):
#                     if G[row + a][column:column + c] != P[a]:
#                         t_find = False
#                         break
#                 if t_find:
#                     is_find = True
#                     break
#             if t_find:
#                 break
#         print 'YES' if t_find else 'NO'


# method 2, the tricky regular expression method.
import re

sys.stdin = open('input05.txt', 'r')
t = int(raw_input().strip())
for a0 in xrange(t):
    R, C = map(int, raw_input().strip().split(' '))
    G = ''
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G += G_t  #form the sour string
    r, c = map(int, raw_input().strip().split(' '))
    P = ''
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        if P_i == 0:
            P += P_t
        else:
            P = P + '\\d{%d}' % (C - c) + P_t

    # find the pattern
    pattern = re.compile(P)
    matched_obj = pattern.search(G)
    while matched_obj and C - matched_obj.start() % C < c:
        matched_obj = pattern.search(G, matched_obj.start() + 1)
    if not matched_obj:
        print 'NO'
    else:
        pos_row = matched_obj.start()/C     # the start point of the 2D pattern
        pos_column = matched_obj.start()%C
        print 'YES'
