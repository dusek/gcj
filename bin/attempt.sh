#!/bin/sh

# Usage: attempt.sh year round problem input_type attempt
#   e.g. attempt.sh 2014 0 A small 2
# Solve problem "year round problem" for $input_type input size and $attempt-th attempt
# Put solution along with packed source code into upload_dir=~/Downloads/gcj_upload

upload_dir="${upload_dir:-$HOME/Downloads/gcj_upload}"
codejam_dir="$HOME/Documents/Projects/Use/codejam-commandline"

year="$1"
round="$2"
problem="$3"
input_type="$4"
attempt="$5"

thisdir="`dirname "$0"`"

io_prefix=${problem}-${input_type}-${attempt}
input=${io_prefix}.in.txt
output=${io_prefix}.out.txt
rm "$upload_dir"/*
${codejam_dir}/gcj_download_input.py --data-directory=${upload_dir} --input-name=${input} ${problem} ${input_type} ${attempt}
"$thisdir/solve.sh" ${year}.${round} ${problem} $upload_dir/$input > $upload_dir/$output
"$thisdir/pack.sh" $year $round $problem
mv "$thisdir"/../../gcj-dusek* "$upload_dir/"
${codejam_dir}/gcj_submit_solution.py --data-directory=${upload_dir} --output-name=${output} --ignore-default-source --add-source=$upload_dir/gcj-dusek* ${problem} ${input_type} ${attempt}