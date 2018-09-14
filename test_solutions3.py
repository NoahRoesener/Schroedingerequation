#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:29:27 2018

@author: eikegroen
"""

import DataInput as di
import solver as slv
import saveOutput as so
import numpy as np
import Inputtests as it
datalines3=it.reader('input_files/Schroedinger3.inp')
start3 = it.getXMin(datalines3)
stop3 = it.getXMax(datalines3)
n3 = it.getNumOfPoints(datalines3)-1
x3=np.linspace(start3, stop3, n3+1)
inttype3 = it.interpolationType(datalines3) #type of interpolation
A3=it.getA(datalines3)
Vx3 =np.asarray_chkfinite(it.getXValues(datalines3), dtype=np.float64, order='C')
Vy3 = np.asarray_chkfinite(it.getYValues(datalines3), dtype=np.float64, order='C')
fvalue3=it.getFirstEigen(datalines3)-1
lvalue3=it.getLastEigen(datalines3)-1
numev33=lvalue3-fvalue3
aa3=it.Eigen(Vx3, Vy3, x3, inttype3, fvalue3, lvalue3,A3,n3)
eival3=aa3[0]
so.saveEigenvaluestest(eival3 , fvalue3, lvalue3,'testfiles/energietest3.dat')
so.savePotentialtest(slv.Potential(Vx3, Vy3, x3, inttype3), x3,'testfiles/potentialtest3.dat')
def test_potential():
    refpot3=di.readCalcPotential('reference_files/potential3.dat')
    pot3=di.readCalcPotential('testfiles/potentialtest3.dat')
    assert np.all(pot3-refpot3<0.01)
    
def test_energies():
    refenergies3=di.readCalcEigenval('reference_files/energies3.dat')
    energies3=di.readCalcEigenval('testfiles/energietest3.dat')
    assert np.all(refenergies3-energies3<0.01 )