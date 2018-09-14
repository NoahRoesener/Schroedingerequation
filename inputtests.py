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

DIRECTORY = os.getcwd()
FILE_EXISTS = os.path.isfile(DIRECTORY+'/schroedinger.inp')

def reader(file):
    """ The functions reads out the input file

    :type file: string
    :param file: the name of the input file

    :rtype: array[]
    :returns: an array with input values
    """
    with open(file, 'r') as ff:
        content = ff.readlines()
    datalines = []

    for line in content:
        newline = line.replace('\n', '')
        location = newline.find('#')
        if location >= 0:
            newline = newline[0:location].strip()
        if newline is not '':
            datalines.append(newline)
    return datalines


def getmass(datalines):
    """Reads out the mass from an array with many specifications.

    :rtype: float
    :returns: Returns the mass of the object.
    """
    mass = float(datalines[0])
    return mass

def getxmax(datalines):
    """Reads out the maximal x-value from an array with many specifications.

    :rtype: float
    :returns: Returns the maximal x-value
    """
    xmax = datalines[1].split()
    xmax = float(xmax[1])
    return xmax

def getxmin(datalines):
    """Reads out the minimal x-value from an array with many specifications.

    :rtype: float
    :returns: Returns the minimall x-value
    """
    xmin = datalines[1].split()
    xmin = float(xmin[0])
    return xmin

def getnumofpoints(datalines):
    """Reads out the amount of numbers to be calculated and plotted afterwards.

    :rtype: float
    :returns: Returns the number of points to be calculated.
    """
    npoints = datalines[1].split()
    npoints = int(npoints[2])
    return npoints

def getfirsteigen(datalines):
    """The function gets the number of the first eigenvalue that is to account.

    :rtype: float
    :returns: Returns the number of the first eigenvalue
    """
    feigen = datalines[2].split()
    feigen = int(feigen[0])
    return feigen

def getlasteigen(datalines):
    """The function gets the number of the last eigenvalue that is to account.

    :rtype: float
    :returns: Returns the number of the last eigenvalue
    """
    leigen = datalines[2].split()
    leigen = int(leigen[1])
    return leigen

def interpolationtype(datalines):
    """The function gets the interpolation type from an array.

    :rtype: string
    :returns: Returns the interpolationtype
    """
    intertype = datalines[3]
    if intertype == 'cspline':
        return 'cubic'
    else:
        return intertype

def interpoints(datalines):
    """The functions gets the number of interpolationpoints from an array.

    :rtype: float
    :returns: Returns number of interpolationpoints
    """
    interppoints = float(datalines[4])
    return interppoints

def getxvalues(datalines):
    """The function gets the given x-values from the schroedinger.inp.

    :rtype: array[float]
    :returns: Returns the given x-value
    """
    coordinatesx = datalines[5:]
    xvalues = []
    for ii in range(0, len(coordinatesx)):
        xpaires = coordinatesx[ii].split()
        xvalues.extend(xpaires)
    xvalues = xvalues[0::2]
    return xvalues

def getyvalues(datalines):
    """The function gets the given y-values from the schroedinger.inp.

    :rtype: array[float]
    :returns: Returns the given y-value
    """
    coordinatesy = datalines[5:]
    yvalues = []
    for ii in range(0, len(coordinatesy)):
        ypaires = coordinatesy[ii].split()
        yvalues.extend(ypaires)
    yvalues = yvalues[1::2]
    return yvalues

def getA(datalines):
    """The function gets a constant which is necessary for the calculations.

    :rtype: float
    :returns: Returns the constant.
    """
    mm = getmass(datalines) #mass of the object
    nn = getnumofpoints(datalines)-1
    if getxmin(datalines) < 0:
        hh = (abs(getxmin(datalines))+abs(getxmax(datalines)))/nn
    else:
        hh = (getxmax(datalines)-getxmin(datalines))/nn
    aa = 1/(mm*hh**2)
    return aa

def eigen(vx, vy, xx, inttype, fvalue, lvalue, aa, nn):
    """The function is calculating the eigenvalues and and eigenvectors.

    :type vx: [float]
    :param vx: x-values of the interpolation points

    :type vy: [float]
    :param vy: y-values of the interpolation points

    :type xx: np.array(float)
    :param xx: x-values

    :type inttype: string
    :param inttype: type of interpolation

    :type fvalue: int
    :param fvalue: first eigenvalue to be calculated

    :type lvalue: int
    :param lvalue: last eigenvalue to be calculated

    :type aa: float
    :param aa: constant for calculation

    :type nn: int
    :param nn: Number of values to be calculated

    :rtype: (np.array(float),np.array(float))
    :returns: Returns a tuple with the the eigenvalues and and eigenvectors
    """

    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(vx, vy, xx, method=inttype)
    elif inttype == 'polynomial':
        coefficients = np.polyfit(vx, vy, 2)
        grid = np.polyval(coefficients, xx)
    dd = grid+aa
    ee = np.zeros(nn)+(-0.5)*aa
    aa = sclin.eigh_tridiagonal(dd, ee, select='i', select_range=(fvalue, lvalue))
    return aa
