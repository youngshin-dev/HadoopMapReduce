import sys
import csv
import collections
# This reducer takes composite keys that are id and hour delimited by '\t'
# For each id, it will maintain current most frequent hour


#for line in sys.stdin:
def reducer():
    reader=csv.reader(sys.stdin, delimiter='\t')
    #data=line.strip()

    old_id = None
    old_hour = None
    prev_max_hour = 0
    current_max_hour=0
    prev_max_count = 0
    current_max_count=0
    count = 1

    for data in reader:

        this_id=data[0]
        this_hour=data[1]

        if old_id != None and old_hour !=None and old_id != this_id:

            if prev_max_count < count:
                prev_max_count=count
                max_hour=old_hour
            print '\t'.join((old_id,str(max_hour)))

            prev_max_count=0
            count = 1

        elif old_id!=None and old_hour!=None and old_id == this_id and old_hour == this_hour:
            count +=1
        elif old_id!=None and old_hour!=None and old_id ==this_id and old_hour != this_hour:
            if prev_max_count < count:
                prev_max_count = count
                max_hour=old_hour
            count=1


        old_hour=this_hour
        old_id=this_id


    if old_id and old_hour:
        if prev_max_count < count:
            prev_max_count = count
            max_hour=old_hour
        print '\t'.join((old_id, str(max_hour)))




test_text ="""\"A\"\t\"2\"
\"A\"\t\"2\"
\"A\"\t\"3\"
\"A\"\t\"3\"
\"A\"\t\"3\"
\"A\"\t\"4\"
\"B\"\t\"1\"
\"B\"\t\"2\"
\"B\"\t\"2\"
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

