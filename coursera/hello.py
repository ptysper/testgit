#!/usr/bin/env python3
import re

fh = open('regex_sum_122193.txt', 'r')
total = 0
for line in fh:
    line = line.rstrip()
    lst = re.findall('[0-9]+', line)
    for elem in lst:
        total = total + int(elem)
print(total)
