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

def getMass():
    mass=float(datalines[0])
    return(float(mass))
    
def getXMax():
    XMax=datalines[1].split()
    XMax=float(XMax[0])
    return(XMax)

def getXMin():
    XMin=datalines[1].split()
    XMin=float(XMin[1])
    return(XMin)

def getNumOfPoints():
    nPoints=datalines[1].split()
    nPoints=int(nPoints[2])
    return(nPoints)


def getFirstEigen():
    fEigen=datalines[2].split()
    fEigen=int(fEigen[0])
    return(fEigen)

def getLastEigen():
    lEigen=datalines[2].split()
    lEigen=int(lEigen[1])
    return(lEigen)
    
def interpolationType():
    interType=datalines[3]
    if intertype == 'cspline':
        return('cubic')
    else:
        return(interType)
    

def interPoints():
    interPoints=float(datalines[4])
    return(interPoints)

