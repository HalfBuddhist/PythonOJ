#!/usr/bin/env python
# coding=utf-8

# my code style
def find_total_topics(a, b):
    topicx = 0
    for idx in xrange(len(a)):
        if a[idx] == '1' or b[idx] == '1':
            topicx += 1
    return topicx


n, m = map(int, raw_input().strip().split(' '))
topic = []
for topic_i in xrange(n):
    topic_t = str(raw_input().strip())
    topic.append(topic_t)

max_topicx = -1
topic_num_2_teams = {}

for a0 in xrange(n):
    for b0 in xrange(a0 + 1, n):
        topoic_num = find_total_topics(topic[a0], topic[b0])
        max_topicx = topoic_num if topoic_num > max_topicx else max_topicx
        topic_num_2_teams[topoic_num] = 1 if not topic_num_2_teams.has_key(topoic_num) \
            else topic_num_2_teams[topoic_num] + 1
print max_topicx
print topic_num_2_teams[max_topicx]


# code style 2
n, m = [int(x) for x in raw_input().split()]
maxi = 0
cnt = 0
inp = [raw_input() for _ in range(n)]
for i in range(0, n):
    for j in range(i + 1, n):
        set_bit = bin(int(inp[i], 2) | (int(inp[j], 2))).count("1")
        if set_bit > maxi:
            maxi = set_bit
            cnt = 1
        elif set_bit == maxi:
            cnt += 1
print maxi
print cnt