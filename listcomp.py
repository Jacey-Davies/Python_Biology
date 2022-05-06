#!/usr/bin/env python3

import sys
import math

print([ x//2 for x in [float(x) for x in sys.argv[1:]] ])
