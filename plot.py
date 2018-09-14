#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:57:11 2018

@author: noah
"""
import numpy as np
import matplotlib.pyplot as plt
import solver as slv
import datainput as di
import argparse

_DESCRIPTION = "Program that solves the onedimensional Schrodinger equation \
                for arbitrary potentials"
PARSER = argparse.ArgumentParser(description=_DESCRIPTION)
MSG = "Scale wavefunctions in plot: (default:1.0)"
PARSER.add_argument("-s", "--scale", default=0.01, help=MSG)
MSG = "Change upper limits of the plot: (default: 2.0)"
PARSER.add_argument("-ulim", "--ulimit", default= 2.0, help=MSG)
MSG = "Change lower limits of the plot: (default: -2.0)"
PARSER.add_argument("-llim", "--llimit", default= -2.0, help=MSG)
ARGS = PARSER.parse_args()
print("\nstarting parameters: ")
if float(ARGS.scale) != float(PARSER.get_default("scale")):
    print("changed scalingfactor to ", ARGS.scale)
else:
    print("scalingfactor is currently set to ", PARSER.get_default("scale"), "\t\t\t\t(default)")
if float(ARGS.ulimit) != float(PARSER.get_default("ulimit")):
    print("Changed upper y-limits to ", ARGS.ulimit)
else:
    print("Upper limits are currently set to ", PARSER.get_default("ulimit"), "\t\t\t\t(default)")
if float(ARGS.llimit) != float(PARSER.get_default("llimit")):
    print("Changed lower y-limits to ", ARGS.llimit)
else:
    print("Lower limits are currently set to ", PARSER.get_default("llimit"), "\t\t\t\t(default)")

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
ERWQ = di.readcalcerwartungquad("expvalues.dat") #squared expected value
ERW = di.readcalcerwartung("expvalues.dat") #expected value
UNSCHAERFE = slv.unschaerfe(ERW, ERWQ) #unschaerfe
EIVA, EIVE = slv.eigen(VX, VY, X, INTTYPE, FVALUE, LVALUE) #eigenvalues and eigenvectors



def plotwavefunc(numev, evec, pot, erw, ev, xx, nn, unschaerfe, scalingfactor, ulimit, llimit):
    """The function plots all the calculated values into two plots. The first
       one inclues only the x-values, the potential, and the expected values.
       The second one the Unschaerfe. It saves the two plots afterwards into
    :type numev: float
    :param numev: Number of eigenvectors

    :type evec: np.array(float)
    :param evec: np.array with eigenvectors

    :type pot: array[float]
    :param pot: saved potential

    :type erw: array [float]
    :param erw: erwartungsvalues

    :type ev: array[float]
    :param ev: erwartungsvalues

    :type xx: array[float]
    :param xx: x-values

    :type nn: float
    :param nn: number of points

    :type unschaerfe: array[float]
    :param unschaerfe: unschaerfevalues
    """
    ii = 0
    plt.figure()
    while ii <= numev:
        vec = evec[:, ii]
        nvec = slv.normalize(vec)
        nvec = float(scalingfactor)*nvec+ev[ii]
        plt.subplot(1, 2, 1) #first plot
        plt.plot(xx, pot)
        plt.title('Potential, eigenstates, Erw(x)')
        plt.plot(np.array(erw), ev, 'x', color='blue')
        plt.plot(xx, nvec)
        plt.xlabel('x[Bohr]')
        plt.ylabel('Energy[Hartree]')
        plt.plot(xx, np.zeros(nn+1)+ev[ii], color='grey')
        plt.xlim(di.getxmin(), di.getxmax())
        plt.ylim(float(llimit), float(ulimit))
        ii += 1
    plt.subplot(1, 2, 2) #second plot
    plt.plot(unschaerfe, ev, 'x', color='blue')
    plt.title('$\sigma_x$')
    plt.xlabel('x[Bohr]')

    plt.savefig("schroedinger.pdf")

plotwavefunc(NUMEV, EIVE, di.readcalcpotential("potential.dat"), ERW, di.readcalceigenval("energies.dat"),
             di.readcalcxvalue("potential.dat"), N, UNSCHAERFE, ARGS.scale, ARGS.ulimit, ARGS.llimit)
