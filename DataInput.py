# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:52:36 2018

@author: noah
"""
import numpy as np
#open file and write into "content"
with open('schroedinger.inp', 'r') as f:
    content = f.readlines()

datalines=[]

for line in content:

    newline = line.replace('\n','')


    location = newline.find('#')

    if location >= 0:

        newline = newline[0:location].strip()

    if newline is not '':
        datalines.append(newline)

print(datalines)



