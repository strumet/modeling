#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

## TODO explain this

import sys
import subprocess, shlex
import re
import pathlib

obj_re = re.compile('obj$', re.IGNORECASE)
obj_filename_re = re.compile('([^\/]+(?!\/))\.obj$', re.IGNORECASE)
under_to_dash = lambda matchgroup: matchgroup.group(0).replace('_', '-')

commit = 'None'

ls_cmd = lambda files: 'ls ' + files
git_status_cmd = lambda *args: 'git status'
git_checkout_cmd = lambda branch: 'git checkout ' + branch
git_diff_from_master_cmd = lambda *args: 'git diff --name-only HEAD...master'
git_merge_master_cmd = lambda *args: 'git merge -m "Merge branch \'master\' into backstage" master'
git_add_cmd = lambda files: 'git add ' + ' '.join(files)
git_commit_cmd = lambda files: 'git commit -m "revision" ' + ' '.join(files)
git_push_cmd = lambda *args: 'git push'
revision_cmd = lambda files: './revision.sh ' + ' '.join(files)
feh_cmd = lambda files: 'feh -Fd ' + ' '.join(files)

class Cmd:
    def __init__(self, cmd, args = False, stdout = False, stderr = False, universal_newlines = False):
        self.cmd = cmd
        self.args = args
        self.stdout = stdout
        self.stderr = stderr
        self.universal_newlines = universal_newlines

cmds = [
        Cmd(git_checkout_cmd, 'backstage'),
        Cmd(git_diff_from_master_cmd, None, subprocess.PIPE, subprocess.PIPE, True),
        ]

progress = list(map(lambda cmd: subprocess.run(shlex.split(cmd.cmd(cmd.args)),
    stdout=cmd.stdout, stderr=cmd.stderr, universal_newlines=cmd.universal_newlines), cmds))

CHANGED_FILES = progress[-1].stdout.strip().split('\n')
OBJ_FILES = [f for f in CHANGED_FILES if obj_re.search(f) and pathlib.Path(f).exists()]
UNDERSCORE_TO_DASH_FILES = [obj_filename_re.sub(under_to_dash, f) for f in OBJ_FILES]
PNG_FILES = [obj_re.sub('png', f) for f in UNDERSCORE_TO_DASH_FILES]

cmds = [
        Cmd(git_merge_master_cmd),
        Cmd(revision_cmd, OBJ_FILES),
        Cmd(git_add_cmd, PNG_FILES),
        Cmd(feh_cmd, PNG_FILES),
        ]

progress = list(map(lambda cmd: subprocess.run(shlex.split(cmd.cmd(cmd.args)),
    stdout=cmd.stdout, stderr=cmd.stderr, universal_newlines=cmd.universal_newlines), cmds))

cmds = [
        Cmd(git_commit_cmd, PNG_FILES),
        Cmd(git_checkout_cmd, 'master'),
        Cmd(git_checkout_cmd, 'backstage -- ' + ' '.join(PNG_FILES)),
        Cmd(git_commit_cmd, PNG_FILES),
        Cmd(git_push_cmd),
        ]

while commit != 'y' and commit != 'n':
    commit = input('Commit?\n(Y/N): ').lower()
if commit == 'y':
    progress = list(map(lambda cmd: subprocess.run(shlex.split(cmd.cmd(cmd.args)),
        stdout=cmd.stdout, stderr=cmd.stderr, universal_newlines=cmd.universal_newlines), cmds))
