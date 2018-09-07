#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:03:18 2018

@author: noah
"""
import numpy as np
import solver as slv
import DataInput as di

def saveEigenvalues(eigenValue, numberOfPoints):
    firstEigenvalue= input("Which is the first Eigenvalue you want to save?")
    lastEigenvalue= input("Which is the last Eigenvalue you want to save?")
    for i in range(firstEigenvalue, lastEigenvalue):
        np.savetxt("energies.dat", eigenValue[i], fmt='%s')

def savePotential():
    pot=slv.Potential(di.getXValues(), di.getYValues(), np.linspace(di.getXMax(),di.getXMin(),di.getNumOfPoints()), di.interpolationType(), di.getFirstEigen(), di.getLastEigen(), di.getNumOfPoints()-1)
    potential=[]
    potential=potential.extend(pot)
    print(pot)
    print(potential)
    for i in range (0, len(pot)):
        potential=potential.append(pot[i])
        print(potential)
        #np.savetxt("potential.dat", potential, delimiter=' ', newline='\n' )
        
a=saveEigenvalues()
