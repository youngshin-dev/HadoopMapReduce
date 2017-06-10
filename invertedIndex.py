import re
import csv

# This can be used as a mapper to count the number of times a certain word is used and to extract the forum_index where the word is used
# thus serving as an inverted index



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
            tokens = re.split(r"[.!?,:;\"()<>\[\]#$=\-\/\s]", body)
            for token in tokens:
                if fantastic.match(str(token)):
                    fantastic_count =fantastic_count+1
                elif fantastically.match(str(token)):
            	  	fantastically_list.append(index)
            	
list_str=' '.join(fantastically_list)
print "%d\t%s"%(fantastic_count,list_str)






