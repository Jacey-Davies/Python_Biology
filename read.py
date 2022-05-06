#!/usr/bin/env python3

import sys

fname = sys.argv[1]
with open(fname, 'r') as handle:
  for line in handle:
    print(line[:-1])

