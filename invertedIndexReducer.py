
import sys

fantastic_count=0
fantastically_list=[]
for line in sys.stdin:
    data = line.split("\t")
    fantastic_count+=int(data[0])
    fantastically_list.append(data[1].split())

fantastically_list=sorted(fantastically_list)
list_str=' '.join(fantastically_list)


print "%d\t%s"%(fantastic_count,list_str)

