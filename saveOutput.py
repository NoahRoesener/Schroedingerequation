#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:03:18 2018

@author: noah
"""
import numpy as np

def saveEigenvalues(eigenValue, fvalue, lvalue):
     """Saves the calculated eigenvalues into a file

     Args:
        eigenValue: The container where the eigenvalues are stored in.
        fvalue: The first eigenvalue to be saved.
        lvalue: The last eigenvalue to be saved.
     """
     chEigen = []
     for ii in range(fvalue, lvalue+1):
          test = eigenValue[ii]
          chEigen.append(test)
     np.savetxt("energies.dat", chEigen, fmt='%s')

def savePotential(pot, x):
     """Saves the calculated potential into a file

     Args:
        pot: The container where the calculated potentials are stored in.
        x: The container where the x-coordinates are stored in.
     """
     potential = []
     coordinates = []
     for ii in range(0, len(pot)):
        coordinates.append(x[ii])
        potential.append(pot[ii])
     np.savetxt("potential.dat", np.transpose([coordinates, potential]))

def saveExpValues(erw, erwq):
     """ The function saves the erwartungsvalues and the squared erwartungsvalues.

     Args:
          erw: The container where the calculated erwartungsvalues are stored in.
          erwq: The container where the calculated and squared erwartungsvalues
               are stored in.
     """
     Erwartung = np.zeros(len(erw))
     ErwartungQuad = np.zeros(len(erwq))
     for ii in range(0, len(erw)):
        Erwartung[ii]=erw[ii]
        ErwartungQuad[ii]=erwq[ii]
     np.savetxt("expvalues.dat", np.transpose([Erwartung, ErwartungQuad]), fmt ='%s')


def saveWavefunc(vec, x):
    x_shape = np.reshape(x, (-1,1))
    rts = np.hstack((x_shape, vec))
    np.savetxt("wavefunction.dat", rts)
