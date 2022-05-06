#!/usr/bin/env python3

import sys

count_list = range(int(sys.argv[1]))
mysum = sum(count_list)
freq_list = [ x/mysum for x in count_list ]

print(freq_list)
