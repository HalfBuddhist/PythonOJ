#!/usr/bin/env python
# coding=utf-8

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
for ele in arr:
    print ele,