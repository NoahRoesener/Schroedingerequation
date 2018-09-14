#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:17:51 2018

@author: eikegroen
"""

import DataInput as di
import solver as slv
import saveOutput as so
import numpy as np
import Inputtests as it
datalines5=it.reader('input_files/Schroedinger5.inp')
start5 = it.getXMin(datalines5)
stop5 = it.getXMax(datalines5)
n5 = it.getNumOfPoints(datalines5)-1
x5=np.linspace(start5, stop5, n5+1)
inttype5 = it.interpolationType(datalines5) #type of interpolation
A5=it.getA(datalines5)
Vx5 =np.asarray_chkfinite(it.getXValues(datalines5), dtype=np.float64, order='C')
Vy5 = np.asarray_chkfinite(it.getYValues(datalines5), dtype=np.float64, order='C')
fvalue5=it.getFirstEigen(datalines5)-1
lvalue5=it.getLastEigen(datalines5)-1
numev5=lvalue5-fvalue5
aa5=it.Eigen(Vx5, Vy5, x5, inttype5, fvalue5, lvalue5,A5,n5)
eival5=aa5[0]
so.saveEigenvaluestest(eival5 , fvalue5, lvalue5,'testfiles/energietest5.dat')
so.savePotentialtest(slv.Potential(Vx5, Vy5, x5, inttype5), x5,'testfiles/potentialtest5.dat')
def test_potential():
    refpot5=di.readCalcPotential('reference_files/potential5.dat')
    pot5=di.readCalcPotential('testfiles/potentialtest5.dat')
    assert np.all(pot5-refpot5<0.01)
    
def test_energies():
    refenergies5=di.readCalcEigenval('reference_files/energies5.dat')
    energies5=di.readCalcEigenval('testfiles/energietest5.dat')
    assert np.all(refenergies5-energies5<0.01 )