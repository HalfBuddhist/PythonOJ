#!/bin/python

N = int(raw_input())
map_addressbook = {}
for a0 in xrange(N):
    name, number = raw_input().strip().split()
    map_addressbook[name] = number
# query
query = raw_input()
while query is not None and query != '':
    print '%s=%s' % (query, map_addressbook[query]) if map_addressbook.has_key(query) else 'Not found'
    query = raw_input()


