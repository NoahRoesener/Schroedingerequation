#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:03:18 2018

@author: noah
"""
import numpy as np

def saveeigenvalues(eigenvalue, fvalue, lvalue):
    """Saves the calculated eigenvalues into a file

    :type eigenvalue: array[float]
    :param eigenvalue: calculated eigenvalues

    :type fvalue: float
    :param fvalue: first value to be saved

    :type lvalue: float
    :param lvalue: last value to be saved
    """
    eigenval = []
    for ii in range(fvalue, lvalue+1):
        test = eigenvalue[ii]
        eigenval.append(test)
    np.savetxt("energies.dat", eigenval, fmt='%s')

def saveeigenvaluestest(eigenValue, fvalue, lvalue, path):
     """Saves the calculated eigenvalues into a file for pytest.
     Args:
        eigenValue: The container where the eigenvalues are stored in.
        fvalue: The first eigenvalue to be saved.
        lvalue: The last eigenvalue to be saved.
        path: Directory to be saved in.
     """
     chEigen = []
     for ii in range(fvalue, lvalue+1):
          test = eigenValue[ii]
          chEigen.append(test)
     np.savetxt(path, chEigen, fmt='%s')

def savepotential(pot, xx):
    """Saves the calculated potential into a file

    :type pot: array[float]
    :param pot: calculated potentials

    :type xx: array[float]
    :param xx: calculated x-values
    """
    potential = []
    coordinates = []
    for ii in range(0, len(pot)):
        coordinates.append(xx[ii])
        potential.append(pot[ii])
    np.savetxt("potential.dat", np.transpose([coordinates, potential]))

def saveexpvalues(erw, erwq):
    """ The function saves the erwartungsvalues and the squared erwartungsvalues.

    :type erw: array[float]
    :param erw: calculated erwartungsvalues

    :type erwq: array[float]
    :param erwq: calculated squared erwartungsvalues
    """
    erwartung = np.zeros(len(erw))
    erwartungquad = np.zeros(len(erwq))
    for ii in range(0, len(erw)):
        erwartung[ii] = erw[ii]
        erwartungquad[ii] = erwq[ii]
    np.savetxt("expvalues.dat", np.transpose([erwartung, erwartungquad]), fmt='%s')

def savepotentialtest(pot, xx, path):
     """Saves the calculated potential into a file for pytest.

     :type pot: array[float]
     :param pot: calculated potential

     :type xx: array[float]
     :param xx: calculated x-values

     :type path: string
     :param path: path of the file
     """
     potential = []
     coordinates = []
     for ii in range(0, len(pot)):
        coordinates.append(xx[ii])
        potential.append(pot[ii])
     np.savetxt(path, np.transpose([coordinates, potential]))
def savewavefunc(vec, xx):
    """The function saves the wavefunctions

    :type vec: array[float]
    :param vec: the calculated eigenvectors

    :type xx: array[float]
    :param xx: calculated x-values

    """
    x_shape = np.reshape(xx, (-1, 1))
    rts = np.hstack((x_shape, vec))
    np.savetxt("wavefunction.dat", rts)
