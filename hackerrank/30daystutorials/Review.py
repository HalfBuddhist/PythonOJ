t = input()
for iter in xrange(t):
    str_t = raw_input().strip()
    print '%s %s'%(str_t[::2], str_t[1::2])