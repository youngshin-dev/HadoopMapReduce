import sys
import re
import csv



fantastic=re.compile('fantastic$',re.IGNORECASE)
fantastically=re.compile('fantastically',re.IGNORECASE)
fantastic_count=0
fantastically_list=[]

with open('forum_node_sample.tsv', 'rb') as csvfile:

    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for	line in	reader:
        leng=len(line)
        if 5<=len(line) <=19:
            body = line[4]
            index = line[0]
            index=index.strip('"')
            #tokens=re.split('<|>|"',body)
            #tokens=re.split('\s|\.|,|!|\?|:|;|"|\(|\)|<|>|[|]|#|\$|=|-|/',body)
            tokens = re.split(r"[.!?,:;\"()<>\[\]#$=\-\/\s]", body)
            for token in tokens:
                if fantastic.match(str(token)):
                    fantastic_count =fantastic_count+1
                elif fantastically.match(str(token)):
            	  	fantastically_list.append(index)
            	
list_str=' '.join(fantastically_list)
print "%d\t%s"%(fantastic_count,list_str)






