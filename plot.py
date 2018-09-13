#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:57:11 2018

@author: noah
"""
import numpy as np
import matplotlib.pyplot as plt
import solver as slv
import DataInput as di

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
ERWQ = di.readcalcerwartungquad() #squared expected value
ERW = di.readcalcerwartung() #expected value
UNSCHAERFE = slv.unschaerfe(ERW, ERWQ) #unschaerfe
EIVA, EIVE = slv.Eigen(VX, VY, X, INTTYPE, FVALUE, LVALUE) #eigenvalues and eigenvectors



def plotwavefunc(numev, evec, pot, erw, ev, xx, nn, unschaerfe):
    """The function plots all the calculated values into two plots. The first
       one inclues only the x-values, the potential, and the expected values.
       The second one the Unschaerfe. It saves the two plots afterwards into

    """
    ii = 0
    plt.figure()
    while ii <= numev:
        vec = evec[:, ii]
        nvec = slv.normalize(vec)
        nvec = 0.01*nvec+ev[ii]
        plt.subplot(1, 2, 1) #first plot
        plt.plot(xx, pot)
        plt.title('Potential, eigenstates, Erw(x)')
        plt.plot(np.array(erw), ev, 'x', color='blue')
        plt.plot(xx, nvec)
        plt.xlabel('x[Bohr]')
        plt.ylabel('Energy[Hartree]')
        plt.plot(xx, np.zeros(nn+1)+ev[ii], color='grey')
        plt.xlim(di.getxmin(), di.getxmax())
        plt.ylim(-10, 2)
        ii += 1
    plt.subplot(1, 2, 2) #second plot
    plt.plot(unschaerfe, ev, 'x', color='blue')
    plt.title('$\sigma_x$')
    plt.xlabel('x[Bohr]')

    plt.savefig("schroedinger.pdf")

plotwavefunc(NUMEV, EIVE, di.readcalcpotential(), ERW, di.readcalceigenval(),
             di.readcalcxvalue(), N, UNSCHAERFE)
