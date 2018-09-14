#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:21:44 2018

@author: eikegroen
"""

import DataInput as di
import solver as slv
import saveOutput as so
import numpy as np
import Inputtests as it
datalines2=it.reader('input_files/Schroedinger2.inp')
start2 = it.getXMin(datalines2)
stop2 = it.getXMax(datalines2)
n2 = it.getNumOfPoints(datalines2)-1
x2=np.linspace(start2, stop2, n2+1)
inttype2 = it.interpolationType(datalines2) #type of interpolation
A2=it.getA(datalines2)
Vx2 =np.asarray_chkfinite(it.getXValues(datalines2), dtype=np.float64, order='C')
Vy2 = np.asarray_chkfinite(it.getYValues(datalines2), dtype=np.float64, order='C')
fvalue2=it.getFirstEigen(datalines2)-1
lvalue2=it.getLastEigen(datalines2)-1
numev2=lvalue2-fvalue2
aa2=it.Eigen(Vx2, Vy2, x2, inttype2, fvalue2, lvalue2,A2,n2)
eival2=aa2[0]
so.saveEigenvaluestest(eival2 , fvalue2, lvalue2,'testfiles/energietest2.dat')
so.savePotentialtest(slv.Potential(Vx2, Vy2, x2, inttype2), x2,'testfiles/potentialtest2.dat')
def test_potential():
    refpot2=di.readCalcPotential('reference_files/potential2.dat')
    pot2=di.readCalcPotential('testfiles/potentialtest2.dat')
    assert np.all(pot2-refpot2<0.01)
    
def test_energies():
    refenergies2=di.readCalcEigenval('reference_files/energies2.dat')
    energies2=di.readCalcEigenval('testfiles/energietest2.dat')
    assert np.all(refenergies2-energies2<0.1)
    