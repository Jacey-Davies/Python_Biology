#!/usr/bin/env python3

import sys

end = sys.argv[1]

mylist = list(range(1, int(end)+1, 1))
for index in list(range(0, len(mylist), 1)):
  print(mylist[index])

print('Done!')
