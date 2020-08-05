#!/usr/bin/env python
# coding=utf-8

h = int(raw_input().strip())
m = int(raw_input().strip())

number_map = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
              10: 'ten',
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
              18: 'eighteen', 19: 'nineteen',
              20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty'}

if m == 0:
    print "%s o'clock" % number_map[h]
elif m == 30:
    print "half past %s" % number_map[h]
else:
    if m > 30:
        out_num = 60 - m
        link_word = 'to'
        adjust = 1
    else:
        out_num = m
        link_word = 'past'
        adjust = 0

    if out_num == 15:
        print 'quarter %s %s'%(link_word, number_map[h+adjust])
    else:
        minutes = 'minutes' if out_num > 1 else 'minute'
        if out_num > 20:
            min_str = number_map[out_num / 10 * 10] + ' ' + number_map[out_num % 10] if out_num % 10 != 0 else number_map[
                out_num / 10 * 10]
        else:
            min_str = number_map[out_num]
        print "%s %s %s %s" % (min_str, minutes, link_word, number_map[h + adjust])


