#!/bin/python

import sys


n = int(raw_input().strip())

for index_it in xrange(n):
    print '%s%s'%(' '*(n-1-index_it),'#'*(index_it+1))