'''
@author: atrivedi
'''
import glob
import re
import time
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

start = time.time()

re_search = ['Your code has been rated at', 'R:', 'C:', 'W:', 'E:', 'F:']

#Change filepath to reflect directory that has the pylint results
filepath = "result/pylint_report"

dictionary_error = {
    'R:':{
        },
    'C:':{
        },
    'W:':{
        },
    'E:':{
        },
    'F:':{
        },
    'score': []
    }
for file in glob.glob(filepath + "*.txt"):
    with open(file, 'r', encoding ="ISO-8859-1") as f:
        line_list = f.readlines()
        line_list = [line.strip() for line in line_list]
        for line in line_list:
            for pattern in re_search:
                if re.search(pattern, line)!=None:
#                     print(pattern)
                    
                    if pattern == 'Your code has been rated at':
#                         score = line.split(' ')[-1].split('/')[0]
                        score  = line[line.find('/')-5:line.find('/')]
                        print(file, score)
                        if 10.00>float(score)>0:
                            dictionary_error['score'].append(float(score))
                            break
                        break
#                         print(float(score))
                    if len(re.findall('\(.*?\)',line))!=0:
#                         print(re.findall('\(.*?\)',line)[-1])
                        if re.findall('\(.*?\)',line)[-1] not in dictionary_error[pattern]:
                            dictionary_error[pattern][re.findall('\(.*?\)',line)[-1]] = 1
                            break
                        else:
                             dictionary_error[pattern][re.findall('\(.*?\)',line)[-1]]+=1
                             break
                        break
                    break

print(dictionary_error)

def bar_plotter(D, key, most_common = 10):
    d = Counter(D)
    D = dict(d.most_common(most_common))
    plt.subplot()
    plt.xlabel('errors')
    plt.ylabel('count')
    plt.title(f'Count of each type of {key} error in pylint')
    plt.bar(range(len(D)), D.values(), align='center')
    plt.xticks(range(len(D)), D.keys())
    plt.show()
    
score_list = dictionary_error.pop('score')
import math
score_list = [math.ceil(score) for score in score_list]

general_error = {
    }

for key in dictionary_error:
    general_error[key] = 0
    for key2 in dictionary_error[key]:
        general_error[key]+=dictionary_error[key][key2]
    bar_plotter(dictionary_error[key], key)

plt.subplot()
plt.xlabel('errors')
plt.ylabel('count')
plt.title("General error count for each type")

plt.bar(range(len(general_error)), general_error.values(), align='center')
plt.xticks(range(len(general_error)), general_error.keys())
plt.show()

score_df = pd.DataFrame({"score":score_list})
score_df.boxplot(column = ["score"], vert =False)

plt.title("Boxplot for score")
plt.show()
print(time.time() - start)
