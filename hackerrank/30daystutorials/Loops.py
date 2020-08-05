#!/bin/python

N = int(raw_input().strip())

for i in range(1, 11):
    print '%d x %d = %d'%(N, i, N*i)