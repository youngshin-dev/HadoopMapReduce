#!/usr/bin/python
import sys

# reducer for Hadoop job to get the total number of hits for each sites.
# The output of this reducer can be used as an input for another MapReduce work to get the top n sites.

old_data=None
hits=0

for line in sys.stdin:
    data=line.strip()

    this_data=data

    if old_data and old_data != this_data:
        print '\t'.join((old_data, str(hits)))
        hits=0

    hits += 1
    old_data = this_data



if old_data != None:
    print '\t'.join((old_data, str(hits)))
