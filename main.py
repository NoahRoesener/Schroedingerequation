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


#aa=slv.Eigen(Vx,Vy,x,inttype,fvalue,lvalue)
#ev=aa[0]
#evec=aa[1]

eiva, eive=slv.Eigen(Vx, Vy, x, inttype, fvalue, lvalue)
so.saveExpValues(slv.Erwartung(eive, numev, x), slv.Erwartungquadrat(eive, numev, x))
so.saveEigenvalues(eiva , fvalue, lvalue)
so.savePotential(slv.Potential(Vx, Vy, x, inttype), x)
so.saveWavefunc(eive, x)
Erwq=di.readCalcErwartungQuad()
Erw=di.readCalcErwartung()
Unschärfe=np.sqrt(np.array(Erwq)-np.array(Erw)*np.array(Erw))


plt.plotWavefunc(numev, eive, di.readCalcPotential(), Erw, di.readCalcEigenval(), di.readCalcXValue(), n, Unschärfe)

