#!/usr/bin/env python
# coding=utf-8

# method1: O(n*max(t)/k) complexity.
# n, k = map(int, raw_input().strip().split())
# t = map(int, raw_input().strip().split())
# page_num = 0
# spe_num = 0
# for a in t:
# pro_start = 1
# while a - k > 0:
#         page_num += 1
#         if pro_start <= page_num <= pro_start + k - 1:
#             spe_num += 1
#         pro_start += k
#         a -= k
#     if a > 0:
#         page_num += 1
#         if pro_start <= page_num <= pro_start + a -1:
#             spe_num += 1
#         pro_start += a
# print spe_num


########################################################################
# method2: O(n) complexity.
import math

n, k = map(int, raw_input().strip().split())
t = map(int, raw_input().strip().split())
page_num = 0
spe_num = 0
if k == 1:
    print t[0]
else:
    for a in t:
        pages = (a - 1) / k + 1  # (a-1)/k + 1 is the added pages.
        m = page_num + 1
        n = page_num + pages
        page_num += pages
        if a < m:
            continue
        else:
            # how many pages to roll to find the special
            po_num = int(math.ceil((float(m - k)) / (k - 1))) if m >= k else 0
            if m <= po_num + m <= n:
                # check speical
                end_pro = (po_num + 1) * k if (po_num + 1) * k <= a else a
                if po_num * k + 1 <= m + po_num <= end_pro:
                    spe_num += 1
                    if end_pro == m + po_num and end_pro != a:
                        spe_num += 1
    print  spe_num