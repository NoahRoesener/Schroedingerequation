#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:57:11 2018

@author: noah
"""
import matplotlib.pyplot as plt

def plotWavefunc(numev, evec, pot, Erw, ev, x):
    plt.figure()
    while ii <= numev:
        vec=evec[:,ii]
        nvec=slv.normalize(vec)
        nvec=40*nvec+ev[ii]
        plt.subplot(1,2,1)
        plt.plot(x,Pot)
        plt.title('Potential, eigenstates, Erw(x)')
        plt.plot(np.array(Erw),ev,'x',color='blue')
        plt.plot(x,nvec)
        plt.xlabel('x[Bohr]')
        plt.ylabel('Energy[Hartree]')
        plt.plot(x,np.zeros(n+1)+ev[ii],color='grey')
        ii+=1
    plt.subplot(1,2,2)
    plt.plot(Unschärfe,ev,'x',color='blue')
    plt.title('$\sigma_x$')
    plt.xlabel('x[Bohr]')