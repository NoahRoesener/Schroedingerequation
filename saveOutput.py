#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:03:18 2018

@author: noah
"""
import numpy as np
import DataInput as di

def saveEigenvalues(eigenValue):
    firstEigenvalue= int(input("Which is the first Eigenvalue you want to save?"))
    lastEigenvalue= int(input("Which is the last Eigenvalue you want to save?"))
    chEigen=[]
    for i in range(firstEigenvalue-1, lastEigenvalue):
        test=eigenValue[i]
        chEigen.append(test)
    np.savetxt("energies.dat", chEigen, fmt='%s')
    return (chEigen)

def savePotential(pot, x):
    potential=[]
    coordinates=[]
    for i in range (0, len(pot)):
        coordinates.append(x[i])
        potential.append(pot[i])
    np.savetxt("potential.dat", np.transpose([coordinates, potential]))
        
def saveWavefunc(vec, x):
    wavefunc=[]
    coordinates=[]
    for i in range(0, len(vec)):
        coordinates.append(x[i])
        wavefunc.append(vec[i])
    np.savetxt("wavefunction.dat", (coordinates, [wavefunc]))
    #np.save("wavefunctions.dat", (coordinates,wavefunc))
    
