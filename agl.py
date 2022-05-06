#!/usr/bin/env python3

import statistics
import sys

gene_lengths = []
GFF_filename = '/home/bryank/shared/BSC2891/Dmel.gff'
feature_type = sys.argv[1]

with open(GFF_filename, 'r') as handle:
  for line in handle:
    if line[0] == '#':
      continue
    linearr = line.split('\t')
    ftype = linearr[2]
    start = int(linearr[3])
    end = int(linearr[4])
    if ftype == feature_type:
      gene_length = end-start+1
      gene_lengths.append(gene_length)

print(statistics.mean(gene_lengths), statistics.stdev(gene_lengths))

