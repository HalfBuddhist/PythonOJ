#!/usr/bin/env python
# coding=utf-8

import datetime

d, m, y = map(int, raw_input().strip().split())
D, M, Y = map(int, raw_input().strip().split())
r_date = datetime.date(y,m,d)
e_date = datetime.date(Y,M,D)

if r_date <= e_date:
    print 0
else:
    if r_date.year != e_date.year:
        print 10000
    elif r_date.month != e_date.month:
        print (r_date.month-e_date.month)*500
    else:
        print (r_date-e_date).days*15
