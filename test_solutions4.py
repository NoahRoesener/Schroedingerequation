#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:13:52 2018

@author: eikegroen
"""

import DataInput as di
import solver as slv
import saveOutput as so
import numpy as np
import Inputtests as it
datalines4=it.reader('input_files/Schroedinger4.inp')
start4 = it.getXMin(datalines4)
stop4 = it.getXMax(datalines4)
n4 = it.getNumOfPoints(datalines4)-1
x4=np.linspace(start4, stop4, n4+1)
inttype4 = it.interpolationType(datalines4) #type of interpolation
A4=it.getA(datalines4)
Vx4 =np.asarray_chkfinite(it.getXValues(datalines4), dtype=np.float64, order='C')
Vy4 = np.asarray_chkfinite(it.getYValues(datalines4), dtype=np.float64, order='C')
fvalue4=it.getFirstEigen(datalines4)-1
lvalue4=it.getLastEigen(datalines4)-1
numev4=lvalue4-fvalue4
aa4=it.Eigen(Vx4, Vy4, x4, inttype4, fvalue4, lvalue4,A4,n4)
eival4=aa4[0]
so.saveEigenvaluestest(eival4 , fvalue4, lvalue4,'testfiles/energietest4.dat')
so.savePotentialtest(slv.Potential(Vx4, Vy4, x4, inttype4), x4,'testfiles/potentialtest4.dat')
def test_potential():
    refpot4=di.readCalcPotential('reference_files/potential4.dat')
    pot4=di.readCalcPotential('testfiles/potentialtest4.dat')
    assert np.all(pot4-refpot4<0.01)
    
def test_energies():
    refenergies4=di.readCalcEigenval('reference_files/energies4.dat')
    energies4=di.readCalcEigenval('testfiles/energietest4.dat')
    assert np.all(refenergies4-energies4<0.01 )