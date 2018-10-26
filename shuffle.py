#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

## Shuffles names of files
## Examples: ./shuffle.py midterm_1/EXE-*.png

import subprocess, shlex
import random
import sys

files = subprocess.run(['ls'] + sys.argv[1:], stdout=subprocess.PIPE)
old_files = files.stdout.decode('utf-8').strip().split('\n')

print(old_files)

new_files = old_files[:]
random.shuffle(new_files)

print(new_files)

for i, f in enumerate(old_files):
    subprocess.run(['mv', f, new_files[i] + '.tmp'])

tmp_files = [f + '.tmp' for f in old_files]

for f in tmp_files:
    subprocess.run(['mv', f, f[:-4]])

