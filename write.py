#!/usr/bin/env python3

import sys

data = [1, 2, 3, 4, 5]
fname = sys.argv[1]
with open(fname, 'w') as outf:
  outf.write('\n'.join([ str(x) for x in data ]))
  outf.write('\n')
