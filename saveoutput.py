#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:03:18 2018

@author: noah
"""
import numpy as np

def saveeigenvalues(eigenvalue, fvalue, lvalue):
    """Saves the calculated eigenvalues into a file

    Args:
        eigenValue: The container where the eigenvalues are stored in.
        fvalue: The first eigenvalue to be saved.
        lvalue: The last eigenvalue to be saved.
    """
    eigenval = []
    for ii in range(fvalue, lvalue+1):
        test = eigenvalue[ii]
        eigenval.append(test)
    np.savetxt("energies.dat", eigenval, fmt='%s')

def savepotential(pot, xx):
    """Saves the calculated potential into a file

    Args:
        pot: The container where the calculated potentials are stored in.
        x: The container where the x-coordinates are stored in.
    """
    potential = []
    coordinates = []
    for ii in range(0, len(pot)):
        coordinates.append(xx[ii])
        potential.append(pot[ii])
    np.savetxt("potential.dat", np.transpose([coordinates, potential]))

def saveexpvalues(erw, erwq):
    """ The function saves the erwartungsvalues and the squared erwartungsvalues.

    Args:
          erw: The container where the calculated erwartungsvalues are stored in.
          erwq: The container where the calculated and squared erwartungsvalues
               are stored in.
    """
    erwartung = np.zeros(len(erw))
    erwartungquad = np.zeros(len(erwq))
    for ii in range(0, len(erw)):
        erwartung[ii] = erw[ii]
        erwartungquad[ii] = erwq[ii]
    np.savetxt("expvalues.dat", np.transpose([erwartung, erwartungquad]), fmt='%s')


def savewavefunc(vec, xx):
    """Moin

    """
    x_shape = np.reshape(xx, (-1, 1))
    rts = np.hstack((x_shape, vec))
    np.savetxt("wavefunction.dat", rts)
