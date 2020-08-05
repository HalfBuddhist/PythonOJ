#!/usr/bin/env python
# coding=utf-8

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

out_str = ''
for ele in s:
    if ele.isalpha():
        if ele.islower():
            out_str += chr((ord(ele) - ord('a') + k) % 26 + ord('a'))
        else:
            out_str += chr((ord(ele) - ord('A') + k) % 26 + ord('A'))
    else:
        out_str += ele
print out_str
