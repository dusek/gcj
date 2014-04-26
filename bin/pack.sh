#!/bin/sh

# Usage: pack.sh year round problem
# Creates an archive named `gcj-dusek-year-round-problem.zip` in the directory parent to the one containing this script.
# The archive contains all source code to reproduce the problem, based on what is in git's head.

year="$1"
round="$2"
problem="$3"

thisdir="`dirname "$0"`"

cd "$thisdir/.."
git archive --prefix=gcj-dusek-$year-$round-problem-$problem/ --output=../gcj-dusek-$year-$round-problem-$problem.zip HEAD README.txt __init__.py bin/ problems/__init__.py problems/$year/__init__.py problems/$year/$round/__init__.py problems/$year/$round/"$problem".{py,c,cpp}

