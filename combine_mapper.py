#!/usr/bin/python

# A mapper for Hadoop job to combine forum_user file and forum_node file. The join is performed on the field 'author_id' in forum_node and 'id' in forum_user
# this mapper will take both files as input and output key,value pairs where the key is a composite key that is consisting of id and a letter to indecate the origin
# The value is the rest of the fields.
#The sample file is my own local file that I extracted from the big file provided by Udacity course " Introduction to Hadoop and MapReduce"


import sys
import csv

reader=csv.reader(sys.stdin,delimiter='\t')
writer=csv.writer(sys.stdout,delimiter='t',quotechar='"',quoting=csv.QUOTE_ALL)

with open('forum_node_sample.tsv','rb') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')

    for line in reader:
            if len(line)==5:
                    id,reputation,gold,silver,bronze=line
                    output=(' '.join((id,'A')), reputation, gold, silver, bronze)
                    print '\t'.join(output)
            if len(line)==19:
                    author_id,title,tagnames,id,node_type,parent_id,abs_parent_id,added_at,score=(line[3],line[1], line[2], line[0], line[5], line[6], line[7], line[8],line[9])
                    #print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(line[0],'B',line[1],line[2],line[3],line[5],line[6],line[7],line[8])
                    print '\t'.join((' '.join((author_id,'B')),title,tagnames,id,node_type,parent_id,abs_parent_id,added_at,score))

