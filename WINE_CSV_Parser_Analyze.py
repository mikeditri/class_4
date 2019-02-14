#!/usr/bin/env python

import os
import numpy as np

myfilename = "wine.data.txt"

with open(myfilename, 'r') as file_handle:
    mylist = []
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(',')
        #print(values)
        linelist = [int,float,float,float,float,int,float,float,float,float,float,float,float,int]
        newlist = [t(x) for t,x in zip(linelist,values)]
        mylist += [newlist]
#print(mylist[0])
#print("")#spacer
rotated_list = [[mylist[jdx][idx]
                for jdx, row in enumerate(mylist)]
                for idx, column in enumerate(mylist[0])]

#print(rotated_list[0])

mean_list = []
sd_list = []

for x in rotated_list:
    mean_list.append(np.mean(x))
    sd_list.append(np.std(x))

print("")
print("List of Means:")
print("")
print(mean_list)

print("")
print("List of Standard Deviations:")
print("")
print(sd_list)

print("")
print('finished!')



        