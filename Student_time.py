import csv
import sys
from datetime import datetime
# mapper for Hadoop job to retrieve for each student, the hour when the student is most active.
# This mapper will output composite keys that are concatenation of author_id and hour.
# Hadoop will shuffle and sort the outputs of the mappers so that for each author_id, the first entry will be

with open('student_test_post_single.csv','rb') as csvfile:
    reader=csv.reader(csvfile, delimiter='\t')
    next(reader, None)
    for line in reader:
        if len(line)==19:
            author_id=line[3]
            added_at=line[8]
            parts=added_at.split(':')
            hour = datetime.strptime(parts[0], "%Y-%m-%d %H").hour
            print '\t'.join((author_id,str(hour)))


