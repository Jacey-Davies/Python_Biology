#!/usr/bin/env python3

import sys
import modeller
import modeller.automodel

alnfname = sys.argv[1]
template = sys.argv[2]
targetse = sys.argv[3]
atomdiry = sys.argv[4]

env = modeller.environ()
env.io.atom_files_directory = [atomdiry]

a = modeller.automodel.automodel(env, alnfname, template, targetse)

a.starting_model = 1
a.ending_model = 1

a.make()
