#!/bin/python

#method 1
n = int(raw_input().strip())
sticks = map(int,raw_input().strip().split(' '))
sticks.sort()
small_stick_idx = 0
cut_mount = 0
total_num = len(sticks)
while small_stick_idx < total_num:
    print total_num - small_stick_idx
    cut_mount += sticks[small_stick_idx] - cut_mount
    while small_stick_idx < total_num and sticks[small_stick_idx] - cut_mount == 0:
        small_stick_idx += 1

#mehtod 2
# N= input()
# num = map(int,raw_input().split())
# val=[0]*1001
# for i in num:
#     val[i]+=1
# counter = 0
# val=val[::-1]
# ans =[]
# for i in val:
#     if i>0:
#         counter += i
#         ans.append(counter)
# ans = ans[::-1]
# for i in ans:
#     print i

#method 3
# N= input()
# num = map(int,raw_input().split())
# val = [0] * 1001
# for i in num:
#     val[i] += 1
# counter = N
#
# ans = [N]
# for i in val:
#     if i > 0:
#         counter -= i
#         ans.append(counter)
#
# # This removes the last element from the result
# # If the input array were empty, removes the value N
# # If not, then removes the value 0
# ans.pop()
#
# for i in ans:
#     print i