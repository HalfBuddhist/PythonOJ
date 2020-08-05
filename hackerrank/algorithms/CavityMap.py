#!/usr/bin/env python
# coding=utf-8

# brute force
n = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)

outstr = ''
for row in xrange(n):
    for column in xrange(n):
        if row == 0 or row == n-1 or column == 0  or column == n-1:
            outstr += grid[row][column]
        else:
            if grid[row][column] > grid[row-1][column] and grid[row][column] > grid[row][column-1] \
                    and grid[row][column] > grid[row+1][column] and grid[row][column]>  grid[row][column+1]:
                # flags[row][column] = 1
                outstr += 'X'
            else:
                outstr += grid[row][column]
    outstr += '\n'

print outstr