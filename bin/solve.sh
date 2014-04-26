#!/bin/sh

# Usage: solve.sh year.round problem input-file
# Solves input-file for specified problem.
# Outputs solution to stdout and progress to stderr.

thisdir="`dirname $0`"
PYTHONPATH="${PYTHONPATH}:${thisdir}/../.." python -m gcj.__init__ "$@"
