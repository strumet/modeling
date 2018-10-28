#!/bin/sh
#
# Get the revisions that has been made and count them

REVISIONS="$(git log --name-only --oneline  | grep '^.*/[0-9]\{6\}.*\.png')"

echo "${REVISIONS}";
echo "\n$(echo "${REVISIONS}" | wc -l) revisions done";
