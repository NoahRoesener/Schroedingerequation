#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:18:66 2018

@author: eikegroen
"""

import datainput as di
import solver as slv
import saveoutput as so
import numpy as np
import inputtests as it
DATALINES6 = it.reader('input_files/Schroedinger6.inp')
START6 = it.getxmin(DATALINES6)
STOP6 = it.getxmax(DATALINES6)
N6 = it.getnumofpoints(DATALINES6)-1
X6 = np.linspace(START6, STOP6, N6+1)
INTTYPE6 = it.interpolationtype(DATALINES6) #type of interpolation
A6 = it.getA(DATALINES6)
VX6 = np.asarray_chkfinite(it.getxvalues(DATALINES6), dtype=np.float64, order='C')
VY6 = np.asarray_chkfinite(it.getyvalues(DATALINES6), dtype=np.float64, order='C')
FVALUE6 = it.getfirsteigen(DATALINES6)-1
LVALUE6 = it.getlasteigen(DATALINES6)-1
NUMEV6 = LVALUE6-FVALUE6
AA6 = it.eigen(VX6, VY6, X6, INTTYPE6, FVALUE6, LVALUE6, A6, N6)
EIVAL6 = AA6[0]
so.saveeigenvaluestest(EIVAL6, FVALUE6, LVALUE6, 'testfiles/energietest6.dat')
so.savepotentialtest(slv.potential(VX6, VY6, X6, INTTYPE6), X6, 'testfiles/potentialtest6.dat')
def test_potential():
    """The funtion tests the potential
    """
    refpot6 = di.readcalcpotential('reference_files/potential6.dat')
    pot6 = di.readcalcpotential('testfiles/potentialtest6.dat')
    assert np.all(pot6-refpot6 < 0.01)

def test_energies():
    """The function tests the energies
    """
    refenergies6 = di.readcalceigenval('reference_files/energies6.dat')
    energies6 = di.readcalceigenval('testfiles/energietest6.dat')
    assert np.all(refenergies6-energies6 < 0.01)