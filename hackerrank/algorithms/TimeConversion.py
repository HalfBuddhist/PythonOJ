#!/bin/python

import sys
import re

time = raw_input().strip()

pattern = r'(\d\d):(\d\d):(\d\d)((AM)|(PM))'

match_result = re.match(pattern, time)

if match_result:
    hours = match_result.group(1)
    minutes = match_result.group(2)
    seconds = match_result.group(3)
    ampm = match_result.group(4)

    if ampm == 'AM':
        print '%s:%s:%s'%(hours if hours!='12' else '00', minutes, seconds)
    elif ampm =='PM':
        print '%s:%s:%s'%(hours if hours=='12' else str(int(hours)+12), minutes, seconds)
