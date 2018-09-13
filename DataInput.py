# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:52:36 2018

@author: noah
"""
import os
import numpy as np

DIRECTORY = os.getcwd()
FILE_EXISTS = os.path.isfile(DIRECTORY+'/schroedinger.inp')
if FILE_EXISTS == True:
    with open('schroedinger.inp', 'r') as f:
        CONTENT = f.readlines()
    DATALINES = []
else:
    FILEDIRECTORY = input("Please specify the place of your inputfile:")
    with open(FILEDIRECTORY, 'r') as f:
        CONTENT = f.readlines()
    DATALINES = []
for line in CONTENT:
    NEWLINE = line.replace('\n', '')
    LOCATION = NEWLINE.find('#')
    if LOCATION >= 0:
        NEWLINE = NEWLINE[0:LOCATION].strip()
    if NEWLINE is not '':
        DATALINES.append(NEWLINE)


def getmass():
    """Reads out the mass from an array with many specifications.

    Return:
        Returns the mass of the object.
    """
    mass = float(DATALINES[0])
    return mass

def getxmax():
    """Reads out the maximal x-value from an array with many specifications.

    Return:
        Returns the maximal x-value
    """
    xmax = DATALINES[1].split()
    xmax = float(xmax[1])
    return xmax

def getxmin():
    """Reads out the minimal x-value from an array with many specifications.

    Return:
        Returns the minimal x-value
    """
    xmin = DATALINES[1].split()
    xmin = float(xmin[0])
    return xmin

def getnumofpoints():
    """Reads out the amount of numbers to be calculated and plotted afterwards.

    Return:
        Returns the number of points to be calculated.
    """
    npoints = DATALINES[1].split()
    npoints = int(npoints[2])
    return npoints

def getfirsteigen():
    """The function gets the number of the first eigenvalue that is to account.

    Return:
        Returns the first number of the eigenvalues that ist to account.
    """
    feigen = DATALINES[2].split()
    feigen = int(feigen[0])
    return feigen

def getlasteigen():
    """The function gets the number of the last eigenvalue that is to account.

    Return:
        Returns the last number of the eigenvalues that ist to account.
    """
    leigen = DATALINES[2].split()
    leigen = int(leigen[1])
    return leigen

def interpolationtype():
    """The function gets the interpolation type from an array.

    Return:
        Returns the interpolation type.
    """
    intertype = DATALINES[3]
    if intertype == 'cspline':
        return 'cubic'
    else:
        return intertype

def interpoints():
    """The functions gets the number of interpolationpoints from an array.

    Return:
         Returns the number of interpolationpoints
    """
    interppoints = float(DATALINES[4])
    return interppoints

def getxvalues():
    """The function gets the given x-values from the schroedinger.inp.

    Return:
          Returns the given x-values.
    """
    coordinatesx = DATALINES[5:]
    xvalues = []
    for ii in range(0, len(coordinatesx)):
        xpaires = coordinatesx[ii].split()
        xvalues.extend(xpaires)
    xvalues = xvalues[0::2]
    return xvalues

def getyvalues():
    """The function gets the given y-values from the schroedinger.inp.

    Return:
          Returns the given y-values
    """
    coordinatesy = DATALINES[5:]
    yvalues = []
    for ii in range(0, len(coordinatesy)):
        ypaires = coordinatesy[ii].split()
        yvalues.extend(ypaires)
    yvalues = yvalues[1::2]
    return yvalues

def readcalceigenval():
    """The function reads out the calculated eigenvalues that are saved in a file.

    Return:
        Returns an array with the eigenvalues as its content.
    """
    with open('energies.dat', 'r') as ff:
        content_energies = ff.readlines()
        energies = []
    for line in content_energies:
        newline = line.replace('\n', '')
        energies.append(newline)
    readenergies = np.zeros(len(energies))
    for ii in range(0, len(energies)):
        readenergies[ii] = float(energies[ii])
    return readenergies

def readcalcpotential():
    """The functon reads out the calculated potentials that are saved in a file.

    Return:
        Returns an array with the potentials as its content.
    """
    with open('potential.dat', 'r') as ff:
        content_potential = ff.readlines()
        potential = []
    for line in content_potential:
        newline = line.replace('\n', '')
        potential.append(newline)
    readpotential = np.zeros(len(potential))
    for ii in range(0, len(potential)):
        readpotential[ii] = float(potential[ii].split()[1])
    return readpotential

def readcalcxvalue():
    """The function reads out the calculated x values that are saved in a file.

    Return:
        Returns an array with the calculated x values as its content.
    """
    with open('potential.dat', 'r') as ff:
        content_potential = ff.readlines()
        potential = []
    for line in content_potential:
        newline = line.replace('\n', '')
        potential.append(newline)
    readcoordinates = np.zeros(len(potential))
    for ii in range(0, len(potential)):
        readcoordinates[ii] = float(potential[ii].split()[0])
    return readcoordinates

def readcalcerwartung():
    """The function reads out the calculated erwartungsvalues that are saved in a file.

    Retun:
        Returns an array with the calculated erwartungsvalues as its content.
    """
    with open('expvalues.dat', 'r') as ff:
        content_expvalues = ff.readlines()
        erwartung = []
    for line in content_expvalues:
        newline = line.replace('\n', '')
        erwartung.append(newline)
    erwartungval = np.zeros(len(erwartung))
    for ii in range(0, len(erwartung)):
        erwartungval[ii] = float(erwartung[ii].split()[0])
    return erwartungval

def readcalcerwartungquad():
    """The function reads out the calculated and squared erwartungsvalues
        that are saved in a file.

    Return:
        Returns an array with the calculated and squared erwartungsvalues as its content.
    """
    with open('expvalues.dat', 'r') as ff:
        content_expvalues = ff.readlines()
        erwartungquad = []
    for line in content_expvalues:
        newline = line.replace('\n', '')
        erwartungquad.append(newline)
    erwartungquadval = np.zeros(len(erwartungquad))
    for ii in range(0, len(erwartungquad)):
        erwartungquadval[ii] = float(erwartungquad[ii].split()[0])
    return erwartungquadval

def readcalcwavefunc():
    """The function reads out the wavefunctions, which are stored in the wavefunction.dat
       and passes it to arrays.

    Return:
         Returns an array with the wavefuntions as its content.
    """
    with open('wavefunction.dat', 'r') as ff:
        content_wavefunc = ff.readlines()
        wavefunc = []
    for line in content_wavefunc:
        newline = line.replace('\n', '')
        wavefunc.append(newline)
    wavefuncval = np.zeros(len(wavefunc), len(wavefunc))
    for ee in range(1, len(wavefunc)):
        for ii in range(0, len(wavefunc)):
            wavefuncval[ee][ii] = float(wavefunc[ii].split()[ee])
    return wavefuncval

#print(readcalcwavefunc())
