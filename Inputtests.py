#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:08:29 2018

@author: eikegroen
"""

import os
import numpy as np
from scipy import linalg as sclin
from scipy.linalg import eigh_tridiagonal
from scipy.interpolate import griddata

directory= os.getcwd()
file_exists=os.path.isfile(directory+'/schroedinger.inp')

def reader(file):
    with open(file, 'r') as f:
        content = f.readlines()
    datalines=[]

    for line in content:
        newline = line.replace('\n','')
        location = newline.find('#')
        if location >= 0:
            newline = newline[0:location].strip()
        if newline is not '':
            datalines.append(newline)
    return datalines


def getMass(datalines):
    """Reads out the mass from an array with many specifications.

    Return:
        Returns the mass of the object.
    """
    mass=float(datalines[0])
    return(float(mass))

def getXMax(datalines):
    """Reads out the maximal x-value from an array with many specifications.

    Return:
        Returns the maximal x-value
    """
    XMax=datalines[1].split()
    XMax=float(XMax[1])
    return(XMax)

def getXMin(datalines):
    """Reads out the minimal x-value from an array with many specifications.

    Return:
        Returns the minimal x-value
    """
    XMin=datalines[1].split()
    XMin=float(XMin[0])
    return(XMin)

def getNumOfPoints(datalines):
    """Reads out the amount of numbers to be calculated and plotted afterwards.

    Return:
        Returns the number of points to be calculated.
    """
    nPoints=datalines[1].split()
    nPoints=int(nPoints[2])
    return(nPoints)

def getFirstEigen(datalines):
    """The function gets the number of the first eigenvalue that is to account.

    Return:
        Returns the first number of the eigenvalues that ist to account.
    """
    fEigen=datalines[2].split()
    fEigen=int(fEigen[0])
    return(fEigen)

def getLastEigen(datalines):
    """The function gets the number of the last eigenvalue that is to account.

    Return:
        Returns the last number of the eigenvalues that ist to account.
    """
    lEigen=datalines[2].split()
    lEigen=int(lEigen[1])
    return(lEigen)

def interpolationType(datalines):
    """The function gets the interpolation type from an array.

    Return:
        Returns the interpolation type.
    """
    interType=datalines[3]
    if interType == 'cspline':
        return('cubic')
    else:
        return(interType)

def interPoints(datalines):
    
    interPoints=float(datalines[4])
    return(interPoints)

def getXValues(datalines):
     """The function gets the given x-values from the schroedinger.inp.

     Return:
          Returns the given x-values.
     """
     coordinatesX=datalines[5:]
     xValues=[]
     for ii in range(0, len(coordinatesX)):
        xPaires=coordinatesX[ii].split()
        xValues.extend(xPaires)
     xValues=xValues[0::2]
     return(xValues)

def getYValues(datalines):
     """The function gets the given y-values from the schroedinger.inp.
     
     :type datalines: [string]
     :param datalines: contains information of the input file
      
     :rtype: [float]
     :returns: Returns the given y-values
     """
     coordinatesY=datalines[5:]
     yValues=[]
     for ii in range(0, len(coordinatesY)):
        yPaires=coordinatesY[ii].split()
        yValues.extend(yPaires)
     yValues=yValues[1::2]
     return(yValues)
     
def getA(datalines):
    """The function gets a constant which is necessary for the calculations.
    
    Return:
        Returns the constant
    """
    M = getMass(datalines) #mass of the object
    N = getNumOfPoints(datalines)-1
    if getXMin(datalines)<0:
        H = (abs(getXMin(datalines))+abs(getXMax(datalines)))/N
    else:
        H = (getXMax(datalines)-getXMin(datalines))/N
    A = 1/(M*H**2)
    return(A)
    
def Eigen(Vx, Vy, x, inttype, fvalue, lvalue, A,N):
    """The function is calculating the eigenvalues and and eigenvectors.
    
    :type Vx: [float]
    :param Vx: x-values of the interpolation points
     
    :type Vy: [float]
    :param Vy: y-values of the interpolation points
     
    :type x: np.array(float)
    :param x: x-values
     
    :type inttype: string
    :param inttype: type of interpolation
     
    :type fvalue: int
    :param fvalue: first eigenvalue to be calculated
     
    :type lvalue: int
    :param lvalue: last eigenvalue to be calculated
     
    :type A: float
    :param A: constant for calculation
     
    :type N: int
    :param N: Number of values to be calculated
      
    :rtype: (np.array(float),np.array(float))
    :returns: Returns a tuple with the the eigenvalues and and eigenvectors
    """
    
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(Vx, Vy, x, method=inttype)
    elif inttype == 'polynomial':
        coefficients = np.polyfit(Vx, Vy, 2)
        grid = np.polyval(coefficients, x)
    d = grid+A
    e = np.zeros(N)+(-0.5)*A
    aa = sclin.eigh_tridiagonal(d, e,select='i',select_range=(fvalue, lvalue))
    return aa
    