#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

## Get multiple pull requests diff or merge at a time.
## Formal checking (for naming or path errors) is possible adding some
## regex rule in the act_dict dictionary.
##
## Launch from repository specifying command  to execute (diff or merge)
## and pull request number.
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

## Formal rules
act_dict = {
        'activities/0/': {
            'regex': re.compile('^\d{6}\.(jpg|png|jpeg)$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'activities/0#activity-0'},
        'activities/1/': {
            'regex': re.compile('^\d{6}[-_]0[1-3][ABC]\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'activities/1#activity-1'},
        'activities/2/': {
            'regex': re.compile('^\d{6}[-_]\d\d(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'activities/2#activity-2'},
        'activities/3/': {
            'regex': re.compile('^\d{6}[-_][ABCF](-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'activities/3#activity-3'},
        'activities/4/': {
            'regex': re.compile('^\d{6}[-_][RP](-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'activities/4#activity-4'},
        'activities/5/': {
            'regex': re.compile('^\d{6}(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'activities/5#activity-5'},
        'exercises/': {
            'regex': re.compile('^\d{6}[-_]\d\d(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'exercises#exercises'},
        'midterm_1/': {
            'regex': re.compile('^\d{6}[-_]\d\d(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'midterm_1#first-midterm'},
        'activities/6/': {
            'regex': re.compile('^\d{6}[-_]\d\d(-LP)?\.obj$', re.IGNORECASE),
            'url': 'https://github.com/strumet/modeling/tree/master/' + \
                    'activities/6#activity-6'},
        }

## Functions
get_range = lambda li: [val for val in range(li[0], li[1]+1)]
get_format = lambda x: get_range(list(map(int, x.split('-')))) if '-' in x \
        else map(int, x.split(',')) 
get_path_index = lambda x: x.rindex('/') + 1 if '/' in x else 1
get_path_url = lambda p: " pubblicata all'indirizzo " + act_dict[p]['url'] \
        if p in act_dict else '.'
## Create mail to send in case of errors
mail_body = lambda id_no, wrong_files, path: (
        "Ciao " + STUD_DICT[id_no][1].capitalize() + ",\n"
        "nella tua consegna sono presenti errori formali relativi ai file:\n"
        "\n" + ('').join(['* ' + f + '\n' for f in wrong_files]) + "\n"
        "Verifica che il nome, il formato e le cartelle dei file inviati "
        "corrispondano a quanto indicato nella pagina di istruzioni "
        "" + get_path_url(path) + "\n"
        "Un saluto,\nmf"
        )

## Variables, containers, regex
CMD = sys.argv[1]
RAW_PR = sys.argv[2:]
NESTED_PR = [get_format(i) for i in RAW_PR]
PR = [item for sublist in NESTED_PR for item in sublist]
## Get students data to prepare mail
STUDENTS_FILE = '/home/mf/Documents/uni/strumod/documents/status.csv'
STUD_LIST = [l.split(';') for l in 
        open(STUDENTS_FILE, encoding="ISO-8859-1").read().split('\n')]
STUD_DICT = {l[0]: l[1:4] for l in 
        STUD_LIST if len(l) > 3 and re.match('\d{6}', l[0])}
##
id_re = re.compile('/(\d{6})')
reports = {}
mails = {}
commands = {
        'diff': lambda x: 'git diff --stat HEAD...origin/pr/' + str(x),
        'merge': lambda x: 'git merge origin/pr/' + str(x)
        }


def main():
    for i in PR:
        print(commands[CMD](i))
        cmd = subprocess.run(shlex.split(commands[CMD](i)),
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                universal_newlines=True)
        print(cmd.stdout)
        if len(cmd.stderr) > 0:
            print(cmd.stderr)
        ## Check formal correctness
        if CMD == 'diff':
            reports[str(i)] = []
            ## Get filenames from diff output
            files = list(map(lambda x: x[:x.index('|')].strip(),
                cmd.stdout.strip().strip().split('\n')[:-1]))
            for f in files:
                path = f[:get_path_index(f)]
                filename = f[get_path_index(f):].replace('_', '-')
                if len(filename) > 0 and (path not in act_dict or
                        not act_dict[path]['regex'].search(filename)):
                    reports[str(i)].append(f)
            ## Remove empty reports
            if len(reports[str(i)]) == 0:
                del reports[str(i)]
            print()

    if CMD == 'diff' and len(reports) > 0:
        ## Create report of wrong files
        for d in reports:
            if len(reports[d]) > 0:
                id_no = id_re.search(reports[d][0]).group(1)
                print(d, ':')
                for f in reports[d]:
                    print('\t', f)
                mails[d] = mail_body(id_no, reports[d], path)
        ## Print out the mail text to send
        send_mail = None
        while send_mail not in ['n', 'y']:
            send_mail = input('\nPrepare mail?\n(y/n): ').lower()
            if send_mail == 'y':
                for m in mails:
                    print('\n' + m + ':\n' + mails[m])


main()
