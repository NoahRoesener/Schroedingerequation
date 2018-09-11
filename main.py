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
import plot as plt

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

aa=slv.Eigen(Vx,Vy,x,inttype,fvalue,lvalue)
ev=aa[0]
evec=aa[1]
Pot=slv.Potential(Vx,Vy,x,inttype)
Erwq=slv.Erwartungquadrat(evec, numev, x)
Erw=slv.Erwartung(evec, numev, x)
Unschärfe=np.sqrt(np.array(Erwq)-np.array(Erw)*np.array(Erw))

so.saveEigenvalues(ev, fvalue, lvalue)
so.savePotential(Pot, x)
so.saveWavefunc(evec, x)


plt.plotWavefunc(numev, evec, Pot, Erw, ev, x)

