#!/usr/bin/env python
# coding=utf-8

import sys, time

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = []
        segs = path.split("/")
        for seg in segs:
            if seg == "" or seg == ".":
                pass
            elif seg == "..":
                if len(paths) > 0:
                    paths.pop()
            else:
                paths.append(seg)
        
        if len(paths) == 0:
            return "/"
        else:
            return "/" + "/".join(paths)

if __name__ == '__main__':
    
    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input
    print(Solution().simplifyPath("/a/./b/../../c/"))
    # resolve   
    # output
    print(time.time() - begin_clock, 'seconds')
