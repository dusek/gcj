#!/bin/sh

upload_dir="${upload_dir:-$HOME/Downloads/gcj_upload}"

year="$1"
round="$2"
problem="$3"

thisdir="`dirname "$0"`"

input=${problem}-*.in.txt
output=$(echo $input | sed -e 's@\.in\.@\.out\.@')
"$thisdir/solve.sh" ${year}.${round} ${problem} $input > $output
"$thisdir/pack.sh" $year $round $problem
rm "$upload_dir"/*
mv "$thisdir"/../../gcj-dusek* "$output" "$upload_dir/"
