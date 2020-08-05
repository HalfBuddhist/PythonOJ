#!/bin/python

#method 1
# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     temp = (pow(2, n/2+1)-1)
#     print temp if not n%2 else temp*2

#method 2
# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     print pow(2, (n+3)/2)-1-n%2

#method 3
# this is a closed form
# a(0) = 1; a(n) = if n is even then a(n-1)+1 else 2*a(n-1).
# for example:
# 1, 2, 3, 6, 7, 14, 15, 30, 31, 62, 63, 126, 127, 254, 255, 510, 511, 1022, 1023, 2046, 2047, 4094,
#  4095, 8190, 8191, 16382, 16383, 32766, 32767, 65534, 65535, 131070, 131071, 262142, 262143, 524286,
# 524287, 1048574, 1048575, 2097150, 2097151
# formula as follow:
# a(0) = 1; for n>=1, a(2*n) = 2^(n+1)-1, a(2*n-1) = 2^(n+1)-2; a(n) = 2^floor((n+3)/2)-3/2+(-1)^n/2.
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print int(pow(2, (n+3)/2)-1.5+pow(-1,n)/2.0)
