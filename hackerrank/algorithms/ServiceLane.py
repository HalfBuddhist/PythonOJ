#!/bin/python

import sys


n,t = map(int, raw_input().strip().split(' '))
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = map(int, raw_input().strip().split(' '))
    print min(width[i:j+1])