#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:48:19 2018

@author: eikegroen
"""
import datainput as di
import solver as slv
import saveoutput as so
import numpy as np
import inputtests as it
DATALINES1 = it.reader('input_files/Schroedinger1.inp')
START1 = it.getxmin(DATALINES1)
STOP1 = it.getxmax(DATALINES1)
N1 = it.getnumofpoints(DATALINES1)-1
X1 = np.linspace(START1, STOP1, N1+1)
INTTYPE1 = it.interpolationtype(DATALINES1) #type of interpolation
A1 = it.getA(DATALINES1)
VX1 = np.asarray_chkfinite(it.getxvalues(DATALINES1), dtype=np.float64, order='C')
VY1 = np.asarray_chkfinite(it.getyvalues(DATALINES1), dtype=np.float64, order='C')
FVALUE1 = it.getfirsteigen(DATALINES1)-1
LVALUE1 = it.getlasteigen(DATALINES1)-1
NUMEV1 = LVALUE1-FVALUE1
AA1 = it.eigen(VX1, VY1, X1, INTTYPE1, FVALUE1, LVALUE1, A1, N1)
EIVAL1 = AA1[0]
so.saveeigenvaluestest(EIVAL1, FVALUE1, LVALUE1, 'testfiles/energietest1.dat')
so.savepotentialtest(slv.potential(VX1, VY1, X1, INTTYPE1), X1, 'testfiles/potentialtest1.dat')
def test_potential1():
    """The funtion tests the potential
    """
    refpot1 = di.readcalcpotential('reference_files/potential1.dat')
    pot1 = di.readcalcpotential('testfiles/potentialtest1.dat')
    assert np.all(pot1-refpot1 < 0.01)

def test_energies1():
    """The function tests the energies
    """
    refenergies1 = di.readcalceigenval('reference_files/energies1.dat')
    energies1 = di.readcalceigenval('testfiles/energietest1.dat')
    assert np.all(refenergies1-energies1 < 0.1)
