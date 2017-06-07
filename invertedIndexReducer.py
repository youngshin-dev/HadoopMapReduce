#!/usr/bin/python
import sys

fantastic_count=0
fantastically_list=[]
test=['0\t 1 2 3 4','2\t5 6 7 8']
for line in test:
    data = line.split("\t")
    fantastic_count+=int(data[0])
    if len(data)==2:
        nums=data[1].split()
        for item in nums:
            fantastically_list.append(int(item))

fantastically_list=sorted(fantastically_list)
list_str=' '.join(str(e) for e in fantastically_list)


print "%d\t%s"%(fantastic_count,list_str)

