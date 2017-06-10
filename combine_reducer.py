#!/usr/bin/python

# This reducer will receive the composite keys that are in sorted order( first sorted by the 'id' and secondly sorted by the letter that indicate the origin (i.e 'A' or 'B')
# It will split the key into two parts.
# Assumption: 'id' is the primary key in the forum_user
# I've provided the test string.

import sys
import csv

def reducer():

    reader=csv.reader(sys.stdin,delimiter='\t')
    writer=csv.writer(sys.stdout,delimiter='t',quotechar='"',quoting=csv.QUOTE_ALL)

    old_key=''
    old_author=''
    user_info=[]

    for data in reader:
        keys=data[0].split(' ')
        this_author=keys[0]
        this_key=keys[1]
        if this_key =='A':
            user_info=data[1:]
        if this_author == old_author and this_key=='B':
            print this_author, '\t'.join(data[1:]), '\t'.join(user_info)
        old_author=this_author


test_text ="""\"100092590 A\"\t\"2\"\t\"0\"\t\"0\"\t\"2\"
\"100092590 B\"\t\"yada\"\t\"bada\"\t\"yada\"\t\"bada\"\t\"yada\"\t\"yada\"\t\"bada\"\t\"yada\"
\"100092590 B\"\t\"yolo\"\t\"bada\"\t\"yada\"\t\"bada\"\t\"yada\"\t\"yada\"\t\"bada\"\t\"bolo\"
\"100092591 A\"\t\"2\"\t\"0\"\t\"0\"\t\"2\"
\"100092591 B\"\t\"yada\"\t\"bada\"\t\"yada\"\t\"bada\"\t\"yada\"\t\"yada\"\t\"bada\"\t\"yada\"
\"100092591 B\"\t\"yolo\"\t\"bada\"\t\"yada\"\t\"bada\"\t\"yada\"\t\"yada\"\t\"bada\"\t\"bolo\"
"""
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    reducer()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()

