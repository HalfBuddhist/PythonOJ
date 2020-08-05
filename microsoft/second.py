#!/usr/bin/env python
# coding=utf-8

def exercise(num, actions, position, act):
    # form the line
    line = [x + 1 for x in xrange(num)]
    for (l, r) in act:
        l -= 1
        r -= 1
        while (0<=l<=num-1) and (0<=r<=num-1) and line[l] < line[r]:
            # interchange
            t = line[l]
            line[l] = line[r]
            line[r] = t
            # update l and r
            l += 1
            r -= 1

    return line[position - 1]