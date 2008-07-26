#!/bin/sh
thisdir="`dirname $0`"
PYTHONPATH="${PYTHONPATH}:${thisdir}/../.." python -m gcj "$@"
