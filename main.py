#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:56:38 2018

@author: noah
"""

import numpy as np
import DataInput as di
import solver as slv
import saveOutput as so
import matplotlib as plt
import scipy as sc

ii=0
plt.figure()
while ii <= numev:
    vec=evec[:,ii]
    nvec=normalize(vec)
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