#!/usr/bin/python
import sys
import csv

# This removes a new line in the body field

csvFile = open('student_test_post_single.csv','wb')
with open('/Users/yourearl82/PycharmProjects/LearnHadoop/student_test_posts.csv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvFile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in tsvin:
        row[4] = row[4].replace("\n", " ").replace("\r"," ")
        csvout.writerow(row)
csvFile.close()