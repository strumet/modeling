#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

## Launch from repository specifying command (diff or merge) and pull request number
## Example:
## ./multi_git.py diff 21,24 27 31-35
## gets the diff (-summary) between HEAD and origin/pr/21,
##                                           origin/pr/24,
##                                           origin/pr/27,
##                                           origin/pr/31,
##                                           origin/pr/32,
##                                           origin/pr/33,
##                                           origin/pr/34,
##                                           origin/pr/35

import sys
import subprocess, shlex

get_range = lambda li: [val for val in range(li[0], li[1]+1)]
get_format = lambda x: get_range(list(map(int, x.split('-')))) if '-' in x else map(int, x.split(',')) 
commands = {
        'diff': lambda x: 'git diff --summary HEAD...origin/pr/' + str(x),
        'merge': lambda x: 'git merge origin/pr/' + str(x)
        }

CMD = sys.argv[1]
RAW_PR = sys.argv[2:]
NESTED_PR = [get_format(i) for i in RAW_PR]
PR = [item for sublist in NESTED_PR for item in sublist]

for i in PR:
    print(commands[CMD](i))
    cmd = subprocess.run(shlex.split(commands[CMD](i)), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print(cmd.stdout)
    print(cmd.stderr)

