# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:52:36 2018

@author: noah
"""
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



def getMass():
    mass=datalines[0]
    return(mass)
    
def getXMax():
    XMax=datalines[1].split()
    XMax=XMax[0]
    return(XMax)

def getXMin():
    XMin=datalines[1].split()
    XMin=XMin[1]
    return(XMin)

def getNumOfPoints():
    nPoints=datalines[1].split()
    nPoints=nPoints[2]
    return(nPoints)

def getFirstEigen():
    fEigen=datalines[2].split()
    fEigen=fEigen[0]
    return(fEigen)

def getLastEigen():
    lEigen=datalines[2].split()
    lEigen=lEigen[1]
    return(lEigen)
    
def interpolationType():
    interType=datalines[3]
    return(interType)

def interPoints():
    interPoints=datalines[4]
    return(interPoints)    