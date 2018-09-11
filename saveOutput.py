#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:03:18 2018

@author: noah
"""
import numpy as np

def saveEigenvalues(eigenValue, fvalue, lvalue):
    chEigen = []
    for i in range(fValue-1, lValue):
        test = eigenValue[i]
        chEigen.append(test)
    np.savetxt("energies.dat", chEigen, fmt ='%s')
    return (chEigen)

def savePotential(pot, x):
    potential = []
    coordinates = []
    for i in range (0, len(pot)):
        coordinates.append(x[i])
        potential.append(pot[i])
    np.savetxt("potential.dat", np.transpose([coordinates, potential]))

def saveWavefunc(vec, x):
    wavefunc = {}
    coordinates = []
    for i in range(0, len(vec)):
        coordinates.append(x[i])
        wavefunc[i]=vec[i]
    #np.savetxt("wavefunction.dat", (coordinates, [wavefunc]))
    #np.save("wavefunctions.dat", (coordinates,wavefunc))    