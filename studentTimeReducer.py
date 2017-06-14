import sys
import csv
import collections
from itertools import takewhile
# This reducer takes composite keys that are id and hour delimited by '\t'
# For each id, it will maintain current most frequent hour
# This version uses counter method to take account for multiple most frequent hours.



#for line in sys.stdin:
def reducer():
    reader=csv.reader(sys.stdin, delimiter='\t')
    #data=line.strip()

    old_id = None
    old_hour = None
    cnt = collections.Counter()

    for data in reader:

        this_id=data[0]
        this_hour=data[1]

        if old_id != None and old_hour !=None and old_id != this_id:
            items=cnt.most_common()
            max_ = items[0][1]
            max_list=list(takewhile(lambda x: x[1] == max_, items))
            for item in max_list:
                print '\t'.join((old_id,str(item[0])))
            cnt = collections.Counter()
            cnt[this_hour]+=1
            old_hour = this_hour
            old_id = this_id


        elif old_id!=None and old_hour!=None and old_id == this_id:
            cnt[this_hour]+=1
            old_hour = this_hour

        elif old_id==None and old_hour==None:
            old_hour=this_hour
            old_id=this_id
            cnt[this_hour] += 1


    if old_id and old_hour:
        items = cnt.most_common()
        max_ = items[0][1]
        max_list = list(takewhile(lambda x: x[1] == max_, items))
        for item in max_list:
            print '\t'.join((old_id, str(item[0])))





test_text ="""\"A\"\t\"1\"
\"A\"\t\"2\"
\"A\"\t\"3\"
\"A\"\t\"3\"
\"A\"\t\"4\"
\"A\"\t\"4\"
\"B\"\t\"1\"
\"B\"\t\"1\"
\"B\"\t\"1\"
\"B\"\t\"3\"
\"B\"\t\"3\"
\"B\"\t\"3\"
"""
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    reducer()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()

