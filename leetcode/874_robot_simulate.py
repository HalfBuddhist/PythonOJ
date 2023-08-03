#!/usr/bin/env python
# coding=utf-8

import sys
import time


class Solution(object):

    def change(self, direction, c):
        if c == -1:
            direction += 1
        elif c == -2:
            direction += 4
            direction -= 1
        return direction % 4

    def forward(self, curx, cury, direction, c, xmap, ymap):
        tarx, tary = curx, cury
        if direction == 0 or direction == 2:
            if direction == 0:
                tary += c
            else:
                tary -= c
            if tarx in xmap:
                obs = xmap[tarx]
                min_dist = -1
                min_ob = 0
                for ob in obs:
                    if (ob > cury and ob <= tary) or (ob < cury and ob >= tary):
                        if min_dist == -1:
                            min_dist = abs(ob-cury)
                            min_ob = ob
                        else:
                            dist = abs(ob-cury)
                            if dist < min_dist:
                                min_dist = abs(ob-cury)
                                min_ob = ob
                if min_dist == -1:
                    return tarx, tary
                else:
                    if cury > min_ob:
                        return tarx, min_ob + 1
                    else:
                        return tarx, min_ob -1
            else:
                return tarx, tary
        elif direction == 1 or direction == 3:
            if direction == 1:
                tarx += c
            else:
                tarx -= c
            if tary in ymap:
                obs = ymap[tary]
                min_dist = -1
                min_ob = 0
                for ob in obs:
                    if (ob > curx and ob <= tarx) or (ob < curx and ob >= tarx):
                        if min_dist == -1:
                            min_dist = abs(ob-curx)
                            min_ob = ob
                        else:
                            dist = abs(ob-curx)
                            if dist < min_dist:
                                min_dist = abs(ob-curx)
                                min_ob = ob
                if min_dist == -1:
                    return tarx, tary
                else:
                    if curx > min_ob:
                        return min_ob + 1, tary
                    else:
                        return min_ob -1, tary
            else:
                return tarx, tary

    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        max_dist = -1
        curx, cury = 0, 0
        # n, e, s, w: 0, 1, 2, 3,
        direction = 0

        xmap = {}
        ymap = {}
        for ob in obstacles:
            if ob[0] in xmap:
                xmap[ob[0]].append(ob[1])
            else:
                xmap[ob[0]] = [ob[1]]
            if ob[1] in ymap:
                ymap[ob[1]].append(ob[0])
            else:
                ymap[ob[1]] = [ob[0]]

        # for x, ylist in xmap:
        #     ylist.sort()
        # for y, xlist in ymap:
        #     xlist.sort()

        for c in commands:
            if c < 0:
                direction = self.change(direction, c)
            else:
                curx, cury = self.forward(curx, cury, direction, c, xmap, ymap)

            dist = curx * curx + cury * cury
            if dist > max_dist:
                max_dist = dist

        return max_dist


if __name__ == '__main__':

    begin_clock = time.time()
    sys.stdin = open('in.txt', 'r')
    # sys.stdout = open('../out.txt', 'w')
    # presolve
    # input

    # resolve
    print(Solution().robotSim([-2,8,3,7,-1], [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]))
    # output
    # print(time.time() - begin_clock, 'seconds')
