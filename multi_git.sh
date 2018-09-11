#!/bin/bash

CMD=$1
START=$2
END=$3

if [ $CMD = 'diff' ]
then
CMD_TXT='git diff --summary HEAD...origin/pr/'
elif [ $CMD = 'merge' ]
then
CMD_TXT='git merge origin/pr/'
else
CMD_TXT='echo NO_COMMAND'
fi

for i in $(seq $START $END); do echo 'PR #'$i; $CMD_TXT$i; done

