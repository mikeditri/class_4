#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

with open(myfilename, 'r') as file_handle:
    mylist = []
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        linelist = [float,float,float,int,float,float,float,float,int,float,float,float,float,float]
        newlist = [t(x) for t,x in zip(linelist,values)]
        mylist += [newlist]
#print(mylist[0])
#print("leaving space")
rotated_list = [[mylist[jdx][idx]
                for jdx, row in enumerate(mylist)]
                for idx, column in enumerate(mylist[0])]

print(rotated_list[0])
print('finished!')



        