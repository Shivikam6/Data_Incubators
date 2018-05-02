import numpy as np
import math
import csv
import pandas as pd
import re
import scipy.stats as stats

wines = pd.read_csv('MT-clean.csv')
########### part (a) ##############

'''wine = []
wine = np.array(wines)
x1 = wine[:,9]         ##9 - Gender
boolarr1 = np.array(x1)

print(boolarr1)
print(boolarr1.shape)
l = len(boolarr1)
count = 0
for i in range (l):
    if (boolarr1[i:i + 1,] == 'M'):
        count = count +1

print("Male count is", count)
print("male/total is ", count/l) #answer is 0.6749749732765495
#print(5005/825118)'''

########### part (b) ############
'''print(wines.shape)
wine = []
wine = np.array(wines)
x1 = wine[:,[21, 26]]         ##21 - is arrested, 26 - out of state
boolarr1 = np.array(x1, dtype=np.bool)

print(boolarr1)
print(boolarr1.shape)

count1 = boolarr1.sum(axis=0)
print(count1)
print(boolarr1[51:52,])
print(len(boolarr1))
if (boolarr1[50:51,0] == boolarr1[50:51,1]):
    print("yes")
else: print("no")
count = 0
for i in range(len(boolarr1)):
    #for j in boolarr1[:,1]:
        if((boolarr1[i:i+1,0] == True) and (boolarr1[i:i+1,1] == True)):
            count = count+1

print("count of true true is", count)
#count2 = boolarr2.sum(axis=0)
#print(count2)''' ## answer is 5005

############ part (d) ############

wine = []
wine = np.array(wines)
x1 = wine[:,14]         ##9 - Gender
boolarr1 = np.array(x1)
#boolarr1 = np.array(x1, dtype=np.bool)

print(boolarr1)
#print(boolarr1.shape)
l = len(boolarr1)
print("length ",l)
count = 0

#p = re.compile('(SPEED)*')
strg = 'SPEED'
for i in boolarr1:
       if strg in str(i):
               count = count + 1

print("Sppeding violation count is ", count)
proportion = count/l
print("proportion of traffic stops in Montana resulted in speeding violations ",proportion) #answer - 0.6580998111785223

##################

stats