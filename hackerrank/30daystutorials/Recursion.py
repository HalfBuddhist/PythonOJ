#!/usr/bin/env python
# coding=utf-8

def factorial(N):
    return  N*factorial(N-1) if N > 0 else 1

N = int(raw_input().strip())
print factorial(N)