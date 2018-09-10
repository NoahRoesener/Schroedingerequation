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
import matplotlib.pyplot as plt
import scipy as sc

start = di.getXMin()
stop = di.getXMax() 
n = di.getNumOfPoints()-1 
x=np.linspace(stop, start, n+1)
inttype = di.interpolationType() #type of interpolation
Vx =np.asarray_chkfinite(di.getXValues(), dtype=np.float64, order='C')
Vy = np.asarray_chkfinite(di.getYValues(), dtype=np.float64, order='C')
fvalue=di.getFirstEigen()-1
lvalue=di.getLastEigen()-1
numev=lvalue-fvalue

aa=slv.Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n)
ev=aa[0]
evec=aa[1]
Pot=slv.Potential(Vx,Vy,x,inttype,fvalue,lvalue,n)
Erwq=slv.Erwartungquadrat(evec, numev, x)
Erw=slv.Erwartung(evec, numev, x)
Unschärfe=np.sqrt(np.array(Erwq)-np.array(Erw)*np.array(Erw))

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