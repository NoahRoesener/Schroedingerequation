# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:52:36 2018

@author: noah
"""
import os 
import numpy as np

directory= os.getcwd()
file_exists=os.path.isfile(directory+'/schroedinger.inp')

if file_exists==True:
    with open('schroedinger.inp', 'r') as f:
        content = f.readlines()
    datalines=[]  
else:
    filedirectory=input("Please specify the place of your inputfile:")
    with open(filedirectory, 'r') as f:
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
    lEigen=int(lEigen[0])
    return(lEigen)
    
def interpolationType():
    interType=datalines[3]
    if interType == 'cspline':
        return('cubic')
    else:
        return(interType)
    
def interPoints():
    interPoints=float(datalines[4])
    return(interPoints)
    
def getXValues():
    coordinatesX=datalines[5:]
    xValues=[]
    for i in range(0, len(coordinatesX)):
        xPaires=coordinatesX[i].split()  
        xValues.extend(xPaires)
    xValues=xValues[0::2]
    test=np.asarray_chkfinite(xValues, dtype=np.float64, order='C')
    return(test) 
    
def getYValues():
    coordinatesY=datalines[5:]
    yValues=[]
    for i in range(0, len(coordinatesY)):
        yPaires=coordinatesY[i].split() 
        for i in range(0, len(yPaires)):
            yPaires[i]=float(yPaires[i])
        yValues.extend(yPaires)
    yValues=yValues[1::2]
    return(yValues) 
