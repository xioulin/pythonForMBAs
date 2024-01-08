import random
from statistics import mean, median,stdev,variance


def generateBustList(number):
    emptyBustList= []
    for i in range(number):
        i=random.randint(35,48)
        emptyBustList.append(i)
    return emptyBustList

bustyList=[43, 46, 47, 43, 40, 45, 37, 44, 47, 35, 45, 48, 35, 36, 39, 48, 35, 46, 45, 43, 42, 37, 48, 38, 42, 40, 40, 48, 47, 37, 46, 42, 35, 36, 42, 42, 42, 41, 47, 40, 40, 47, 41, 43, 47, 39, 41, 39, 43, 42]

import matplotlib.pyplot as plt
from collections import Counter
counter = Counter(bustyList)
# plt.bar(counter.keys(),counter.values())
# plt.show()

hist1={}
for i in bustyList:
    hist1[i]= hist1.get(i,0)+1
n= float(len(bustyList))
pmf={}
for x,freq in hist1.items():
    pmf[x]= freq/n

# plt.bar(pmf.keys(),pmf.values())
# plt.show()







