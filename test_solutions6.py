#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:18:46 2018

@author: eikegroen
"""

import DataInput as di
import solver as slv
import saveOutput as so
import numpy as np
import Inputtests as it
datalines6=it.reader('input_files/Schroedinger6.inp')
start6 = it.getXMin(datalines6)
stop6 = it.getXMax(datalines6)
n6 = it.getNumOfPoints(datalines6)-1
x6=np.linspace(start6, stop6, n6+1)
inttype6 = it.interpolationType(datalines6) #type of interpolation
A6=it.getA(datalines6)
Vx6 =np.asarray_chkfinite(it.getXValues(datalines6), dtype=np.float64, order='C')
Vy6 = np.asarray_chkfinite(it.getYValues(datalines6), dtype=np.float64, order='C')
fvalue6=it.getFirstEigen(datalines6)-1
lvalue6=it.getLastEigen(datalines6)-1
numev6=lvalue6-fvalue6
aa6=it.Eigen(Vx6, Vy6, x6, inttype6, fvalue6, lvalue6,A6,n6)
eival6=aa6[0]
so.saveEigenvaluestest(eival6 , fvalue6, lvalue6,'testfiles/energietest6.dat')
so.savePotentialtest(slv.Potential(Vx6, Vy6, x6, inttype6), x6,'testfiles/potentialtest6.dat')
def test_potential():
    refpot6=di.readCalcPotential('reference_files/potential6.dat')
    pot6=di.readCalcPotential('testfiles/potentialtest6.dat')
    assert np.all(pot6-refpot6<0.01)
    
def test_energies():
    refenergies6=di.readCalcEigenval('reference_files/energies6.dat')
    energies6=di.readCalcEigenval('testfiles/energietest6.dat')
    assert np.all(refenergies6-energies6<0.01 )