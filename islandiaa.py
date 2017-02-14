import re
import codecs
pattern = r'</teiHeader>'
pattern2 = r'<w lemma=".*" type=".*">.*</w>'
tmp = 0;
dic = {}
file_output = codecs.open("Res.txt", 'w')
with open('islandiaaa.xml') as file:
    for row in file:
        tmp+=1;
        if(re.match(pattern,row)):
        	strings=tmp;
        if(re.match(pattern2,row)):
        	arr = row.split("\"")
        	key = arr[3]
        	if(key in dic):
        		dic[key]=dic[key]+1
        	else:
        		dic[key] = 1;
    file_output.write(str(strings)+'\r\n')
    for key, value in dic.items():
    	file_output.write(key+" "+str(value)+"\r\n")
 
file_output.close()
