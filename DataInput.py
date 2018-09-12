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
    """Reads out the mass from an array with many specifications.

    Return:
        Returns the mass of the object.
    """
    mass=float(datalines[0])
    return(float(mass))

def getXMax():
    """Reads out the maximal x-value from an array with many specifications.

    Return:
        Returns the maximal x-value
    """
    XMax=datalines[1].split()
    XMax=float(XMax[1])
    return(XMax)

def getXMin():
    """Reads out the minimal x-value from an array with many specifications.

    Return:
        Returns the minimal x-value
    """
    XMin=datalines[1].split()
    XMin=float(XMin[0])
    return(XMin)

def getNumOfPoints():
    """Reads out the amount of numbers to be calculated and plotted afterwards.

    Return:
        Returns the number of points to be calculated.
    """
    nPoints=datalines[1].split()
    nPoints=int(nPoints[2])
    return(nPoints)

def getFirstEigen():
    """The function gets the number of the first eigenvalue that is to account.

    Return:
        Returns the first number of the eigenvalues that ist to account.
    """
    fEigen=datalines[2].split()
    fEigen=int(fEigen[0])
    return(fEigen)

def getLastEigen():
    """The function gets the number of the last eigenvalue that is to account.

    Return:
        Returns the last number of the eigenvalues that ist to account.
    """
    lEigen=datalines[2].split()
    lEigen=int(lEigen[1])
    return(lEigen)

def interpolationType():
    """The function gets the interpolation type from an array.

    Return:
        Returns the interpolation type.
    """
    interType=datalines[3]
    if interType == 'cspline':
        return('cubic')
    else:
        return(interType)

def interPoints():
    interPoints=float(datalines[4])
    return(interPoints)

def getXValues():
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

def getYValues():
     """The function gets the given y-values from the schroedinger.inp.

     Return:
          Returns the given y-values
     """
    coordinatesY=datalines[5:]
    yValues=[]
    for ii in range(0, len(coordinatesY)):
        yPaires=coordinatesY[ii].split()
        yValues.extend(yPaires)
    yValues=yValues[1::2]
    return(yValues)

def readCalcEigenval():
    """The function reads out the calculated eigenvalues that are saved in a file.

    Return:
        Returns an array with the eigenvalues as its content.
    """
    with open('energies.dat', 'r') as f:
        content_energies = f.readlines()
        energies = []
    for line in content_energies:
        newline = line.replace('\n','')
        energies.append(newline)
    readEnergies=np.zeros(len(energies))
    for ii in range(0, len(energies)):
        readEnergies[ii] = float(energies[ii])
    return (readEnergies)

def readCalcPotential():
    """The functon reads out the calculated potentials that are saved in a file.

    Return:
        Returns an array with the potentials as its content.
    """
    with open('potential.dat', 'r') as f:
        content_potential = f.readlines()
        potential= []
    for line in content_potential:
        newline = line.replace('\n','')
        potential.append(newline)
    readPotential=np.zeros(len(potential))
    for ii in range(0, len(potential)):
        readPotential[ii] = float(potential[ii].split()[1])
    return (readPotential)

def readCalcXValue():
    """The function reads out the calculated x values that are saved in a file.

    Return:
        Returns an array with the calculated x values as its content.
    """
    with open('potential.dat', 'r') as f:
        content_potential = f.readlines()
        potential= []
    for line in content_potential:
        newline = line.replace('\n','')
        potential.append(newline)
    readCoordinates=np.zeros(len(potential))
    for ii in range(0, len(potential)):
        readCoordinates[ii] = float(potential[ii].split()[0])
    return (readCoordinates)

def readCalcErwartung():
    """The function reads out the calculated erwartungsvalues that are saved in a file.

    Retun:
        Returns an array with the calculated erwartungsvalues as its content.
    """
    with open('expvalues.dat', 'r') as f:
        content_expvalues = f.readlines()
        erwartung= []
    for line in content_expvalues:
        newline = line.replace('\n','')
        erwartung.append(newline)
    erwartungval=np.zeros(len(erwartung))
    for ii in range(0, len(erwartung)):
        erwartungval[ii] = float(erwartung[ii].split()[0])
    return (erwartungval)

def readCalcErwartungQuad():
    """The function reads out the calculated and squared erwartungsvalues
        that are saved in a file.

    Return:
        Returns an array with the calculated and squared erwartungsvalues as its content.
    """
    with open('expvalues.dat', 'r') as f:
        content_expvalues = f.readlines()
        erwartungquad= []
    for line in content_expvalues:
        newline = line.replace('\n','')
        erwartungquad.append(newline)
    erwartungquadval=np.zeros(len(erwartungquad))
    for ii in range(0, len(erwartungquad)):
        erwartungquadval[ii] = float(erwartungquad[ii].split()[0])
    return (erwartungquadval)

