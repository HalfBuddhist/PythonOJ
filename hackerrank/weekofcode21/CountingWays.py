#!/usr/bin/env python
# coding=utf-8
import time

begin_clock = time.clock()
n = int(raw_input())
a = [int(x) for x in raw_input().split()]
L, R = map(int, raw_input().split())

mod = long(1E9 + 7)
# maxx = long(1E17 + 5)
maxx = long(1400100)
# maxx = 10
f = list()
f.append([1] * n)

for i in xrange(1, maxx):
    f.append([0] * n)
    for j in xrange(n):
        if j > 0:
            f[i][j] = f[i][j - 1]
        if i >= a[j]:
            f[i][j] += f[i - a[j]][j]
            if f[i][j] >= mod:
                f[i][j] -= mod

res = 0
for i in xrange(L, R + 1):
    res += f[i][n - 1]
    if res >= mod:
        res -= mod
print res

print time.clock()-begin_clock