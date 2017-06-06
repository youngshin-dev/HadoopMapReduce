import sys
import re



for line in sys.stdin:
    data = line.split("\t")
    fantastic=re.compile('fantastic')
    fantastically=re.compile('fantastically')
    fantastic_count=0
    fantastically_list=[]
    if len(data)==20:
        for	line in	data:
            body = line[4]
            index = line[0]
            tokens=re.split(' |.|,|!|\?|:|;|"|(|)|<|>|[|]#|$|=|-|/',body)
            for token in tokens:
                if fantastic.IGNORECASE(token):
                    fantastic_count =fantastic_count+1
                elif fantastically.IGNORECASE(token):
                    fantastically_list.append(index)
list_str=' '.join(fantastically_list)
print "%d\t%s"%(fantastic_count,list_str)





