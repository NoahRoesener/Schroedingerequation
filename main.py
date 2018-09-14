#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:56:38 2018

@author: noah
"""
import argparse
import numpy as np
import datainput as di
import solver as slv
import saveoutput as so

# optional arguments
_DESCRIPTION = "Program that solves the onedimensional Schrodinger equation \
                for arbitrary potentials"
PARSER = argparse.ArgumentParser(description=_DESCRIPTION)
MSG = "Please specify the directory where the inputfile is located: (default: .)"
PARSER.add_argument("-d", "--directory", default=".", help=MSG)
ARGS = PARSER.parse_args()
PATH = "{}/schroedinger.inp".format(ARGS.directory)
print("\nstarting parameters: ")
START = di.getxmin() #minimal x-value
STOP = di.getxmax() #maximal x-value
N = di.getnumofpoints()-1 #Number of interpolation points
X = np.linspace(STOP, START, N+1) #x-values
INTTYPE = di.interpolationtype() #type of interpolation
VX = np.asarray_chkfinite(di.getxvalues(), dtype=np.float64, order='C')
VY = np.asarray_chkfinite(di.getyvalues(), dtype=np.float64, order='C')
FVALUE = di.getfirsteigen()-1 #first eigenvalue
LVALUE = di.getlasteigen()-1 #last eigenvalue
NUMEV = LVALUE-FVALUE #number of eigenvector
EIVA, EIVE = slv.eigen(VX, VY, X, INTTYPE, FVALUE, LVALUE) #eigenvalue and eigenvector

#saving values into files
so.saveexpvalues(slv.erwartung(EIVE, NUMEV, X), slv.erwartungquadrat(EIVE, NUMEV, X))
so.saveeigenvalues(EIVA, FVALUE, LVALUE)
so.savepotential(slv.potential(VX, VY, X, INTTYPE), X)
so.savewavefunc(EIVE, X)

