#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:48:19 2018

@author: eikegroen
"""
import DataInput as di
import solver as slv
import saveOutput as so
import numpy as np
import Inputtests as it
datalines1=it.reader('input_files/Schroedinger1.inp')
start1 = it.getXMin(datalines1)
stop1 = it.getXMax(datalines1)
n1 = it.getNumOfPoints(datalines1)-1
x1=np.linspace(start1, stop1, n1+1)
inttype1 = it.interpolationType(datalines1) #type of interpolation
A1=it.getA(datalines1)
Vx1 =np.asarray_chkfinite(it.getXValues(datalines1), dtype=np.float64, order='C')
Vy1 = np.asarray_chkfinite(it.getYValues(datalines1), dtype=np.float64, order='C')
fvalue1=it.getFirstEigen(datalines1)-1
lvalue1=it.getLastEigen(datalines1)-1
numev1=lvalue1-fvalue1
aa1=it.Eigen(Vx1, Vy1, x1, inttype1, fvalue1, lvalue1,A1,n1)
eival1=aa1[0]
so.saveEigenvaluestest(eival1 , fvalue1, lvalue1,'testfiles/energietest1.dat')
so.savePotentialtest(slv.Potential(Vx1, Vy1, x1, inttype1), x1,'testfiles/potentialtest1.dat')
def test_potential1():
    refpot1=di.readCalcPotential('reference_files/potential1.dat')
    pot1=di.readCalcPotential('testfiles/potentialtest1.dat')
    assert np.all(pot1-refpot1<0.01)
    
def test_energies1():
    refenergies1=di.readCalcEigenval('reference_files/energies1.dat')
    energies1=di.readCalcEigenval('testfiles/energietest1.dat')
    assert np.all(refenergies1-energies1<0.1)
    