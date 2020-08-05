#!/usr/bin/env python
# coding=utf-8
__author__ = 'Qingwei'

n = int(raw_input().strip())
print max(map(len, bin(n)[2:].split('0')))
