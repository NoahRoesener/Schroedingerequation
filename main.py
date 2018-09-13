#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:56:38 2018

@author: noah
"""
import argparse
import numpy as np
import DataInput as di
import solver as slv
import saveoutput as so
import plot as plt

# optional arguments
_DESCRIPTION = "Program that solves the onedimensional Schrodinger equation \
                for arbitrary potentials"
PARSER = argparse.ArgumentParser(description=_DESCRIPTION)
MSG = "Please specify the directory where the inputfile is located: (default: .)"
PARSER.add_argument("-d", "--directory", default=".", help=MSG)
MSG = "Scale wavefunctions in plot: (default:1.0)"
PARSER.add_argument("-s", "--stretch", default=0.01, help=MSG)
ARGS = PARSER.parse_args()
PATH = "{}/schroedinger.inp".format(ARGS.directory)
print("\nstarting parameters: ")
if float(ARGS.stretch) != float(PARSER.get_default("stretch")):
    print("changed scalingfactor to ", ARGS.stretch)
else:
    print("scalingfactor is currently set to ", PARSER.get_default("stretch"), "\t\t\t\t(default)")
START = di.getxmin() #minimal x-value
STOP = di.getxmax() #maximal x-value
N = di.getnumofpoints()-1 #Number of interpolation points
X = np.linspace(STOP, START, N+1) #x-values
INTTYPE = di.interpolationtype() #type of interpolation
VX = np.asarray_chkfinite(di.getxvalues(), dtype=np.float64, order='C')
VY = np.asarray_chkfinite(di.getyvalues(), dtype=np.float64, order='C')
FVALUE = di.getfirsteigen()-1 #first eigenvalue
LVALUE = di.getlasteigen()-1 #last eigenvalue
NUMEV = LVALUE-FVALUE

EIVA, EIVE = slv.Eigen(VX, VY, X, INTTYPE, FVALUE, LVALUE)
so.saveexpvalues(slv.Erwartung(EIVE, NUMEV, X), slv.Erwartungquadrat(EIVE, NUMEV, X))
so.saveeigenvalues(EIVA, FVALUE, LVALUE)
so.savepotential(slv.Potential(VX, VY, X, INTTYPE), X)
so.savewavefunc(EIVE, X)

