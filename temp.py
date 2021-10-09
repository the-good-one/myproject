import pandas as pd
import re
import time
start=time.time()
fre_dic = pd.read_csv("C:\\Users\\ELCOT\\Desktop\\transe\\french_dictionary.csv", header=None)
eng_list = fre_dic[0].to_list()
fre_list = fre_dic[1].to_list()
#def intersection(lst1, lst2): 
#    lst3 = [value for value in lst1 if value in lst2] 
#    return lst3
#lst = intersection(words_list, eng_list)
dic = dict(zip(eng_list,fre_list))
with open("C:\\Users\\ELCOT\\Desktop\\translator\\t8.shakespeare.txt", 'r') as file:
    data = file.read()
def replaceWords(text, wordDict):
   
    check=[]
    frequency = []
    for key in wordDict:
        frequency.append([a.start() for a in re.finditer(key, text)])
        text = text.replace(key, wordDict[key])
#        check.append([a.start() for a in re.finditer(wordDict[key], text)])
    return text,frequency
str1,frequency = replaceWords(data, dic)
freq = []
for i in range(len(frequency)):
    freq.append(len(frequency[i]))

text_file = open("C:\\Users\\ELCOT\\Desktop\\translator\\t8.shakespeare.translated.txt", "w")
text_file.write(" %s " % str1)
text_file.close()

Dict=[{'English':eng, 'French':fre, 'Frequency':fr} for eng,fre,fr in zip(eng_list,fre_list,freq)]
df = pd.DataFrame (Dict, columns = ['English','French','Frequency'])
df.to_csv('C:\\Users\\ELCOT\\Desktop\\translator\\frequency.csv', index=None)
end = time.time()
t=end - start
print("Runtime is {}".format(t))
import os, psutil
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

mem_file = open("C:\\Users\\ELCOT\\Desktop\\translator\\performance.txt", "w")
str_1 = "Time to process: " + str(t) + "secs"
str_2 = "Memory used: " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2) + "mB"
mem_file.write(" %s\n " % str_1)
mem_file.write(" %s " % str_2)
mem_file.close()