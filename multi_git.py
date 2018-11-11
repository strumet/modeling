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
import re

act_dict = {
        'activities/0/': {
            'regex': re.compile('^\d{6}\.(jpg|png|jpeg)$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/activities/0#activity-0'},
        'activities/1/': {
            'regex': re.compile('^\d{6}[-_]0[1-3][ABC]\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/activities/1#activity-1'},
        'activities/2/': {
            'regex': re.compile('^\d{6}[-_]\d\d(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/activities/2#activity-2'},
        'activities/3/': {
            'regex': re.compile('^\d{6}[-_][ABCF](-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/activities/3#activity-3'},
        'activities/4/': {
            'regex': re.compile('^\d{6}[-_][RP](-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/activities/4#activity-4'},
        'exercises/': {
            'regex': re.compile('^\d{6}[-_]\d\d(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/exercises#exercises'},
        'midterm_1/': {
            'regex': re.compile('^\d{6}[-_]\d\d(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/midterm_1#first-midterm'},
        }

reports = {}
mails = {}

id_re = re.compile('/(\d{6})')
get_range = lambda li: [val for val in range(li[0], li[1]+1)]
get_format = lambda x: get_range(list(map(int, x.split('-')))) if '-' in x else map(int, x.split(',')) 
check_file = lambda x: 'git diff --stat --name-only HEAD...origin/pr/' + str(x)
get_path_index = lambda x: x.rindex('/') + 1 if '/' in x else 1
get_path_url = lambda p: " pubblicata all'indirizzo " + act_dict[p]['url'] if p in act_dict else '.'
mail_body = lambda id_no, wrong_files, path: "Ciao " + STUD_DICT[id_no][1].capitalize() + ",\n" + \
        "nella tua consegna sono presenti errori formali relativi ai file:\n\n" + \
        ('').join(['* ' + f + '\n' for f in wrong_files]) + "\n" + \
       "Verifica che il nome, il formato e le cartelle dei file inviati corrispondano a " + \
       "quanto indicato nella pagina di istruzioni" + get_path_url(path) + \
       "\nUn saluto,\nmf"
commands = {
        'diff': lambda x: 'git diff --stat HEAD...origin/pr/' + str(x),
        'merge': lambda x: 'git merge origin/pr/' + str(x)
        }

CMD = sys.argv[1]
RAW_PR = sys.argv[2:]
NESTED_PR = [get_format(i) for i in RAW_PR]
PR = [item for sublist in NESTED_PR for item in sublist]
STUDENTS_FILE = '/home/mf/Documents/uni/strumod/documents/status.csv'
STUD_LIST = [l.split(';') for l in open(STUDENTS_FILE, encoding="ISO-8859-1").read().split('\n')]
STUD_DICT = {l[0]: l[1:4] for l in STUD_LIST if len(l) > 3 and re.match('\d{6}', l[0])}


def main():
    for i in PR:
        print(commands[CMD](i))
        cmd = subprocess.run(shlex.split(commands[CMD](i)), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                universal_newlines=True)
        print(cmd.stdout)
        if len(cmd.stderr) > 0:
            print(cmd.stderr)
        ## Check formal correctness
        if CMD == 'diff':
            reports[str(i)] = []
            check = subprocess.run(shlex.split(check_file(i)), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    universal_newlines=True)
            files = check.stdout.strip().split('\n')
            for f in files:
                path = f[:get_path_index(f)]
                filename = f[get_path_index(f):].replace('_', '-')
                if len(filename) > 0 and (path not in act_dict or not act_dict[path]['regex'].search(filename)):
                    reports[str(i)].append(f)
            print()

    if CMD == 'diff':
    ## Create report of wrong files
        for d in reports:
            if len(reports[d]) > 0:
                id_no = id_re.search(reports[d][0]).group(1)
                print(d, ':')
                for f in reports[d]:
                    print('\t', f)
                mails[d] = mail_body(id_no, reports[d], path)
    ## Print out the mail text to send
        mail = input('\nPrepare mail?\n(y/n): ').lower()
        if mail == 'y':
            for m in mails:
                print('\n' + m + ':\n' + mails[m])


main()
