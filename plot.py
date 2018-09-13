#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:57:11 2018

@author: noah
"""
import matplotlib.pyplot as plt
import solver as slv
import numpy as np
import DataInput as di

def plotWavefunc(numev, evec, pot, Erw, ev, x , n, Unschaerfe):
    ii=0
    plt.figure()
    while ii <= numev:
        vec=evec[:,ii]
        nvec=slv.normalize(vec)
        nvec=0.01*nvec+ev[ii]
        plt.subplot(1,2,1)
        plt.plot(x, pot)
        plt.title('Potential, eigenstates, Erw(x)')
        plt.plot(np.array(Erw),ev,'x',color='blue')
        plt.plot(x,nvec)
        plt.xlabel('x[Bohr]')
        plt.ylabel('Energy[Hartree]')
        plt.plot(x,np.zeros(n+1)+ev[ii],color='grey')
        plt.xlim(di.getXMin(), di.getXMax())
        plt.ylim(0, 4.5)
        ii+=1
    plt.subplot(1,2,2)
    plt.plot(Unschaerfe,ev,'x',color='blue')
    plt.title('$\sigma_x$')
    plt.xlabel('x[Bohr]')