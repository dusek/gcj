#!/bin/sh
year="$1"
round="$2"
problem="$3"

thisdir="`dirname "$0"`"

cd "$thisdir/.."
git archive --prefix=gcj-dusek-$year-$round-problem-$problem/ --output=../gcj-dusek-$year-$round-problem-$problem.zip HEAD README.txt __init__.py bin/ problems/__init__.py problems/$year/__init__.py problems/$year/$round/__init__.py problems/$year/$round/"$problem".{py,c,cpp}

