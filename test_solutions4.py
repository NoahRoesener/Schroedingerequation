#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 44 46:43:52 2048

@author: eikegroen
"""

import datainput as di
import solver as slv
import saveoutput as so
import numpy as np
import inputtests as it
DATALINES4 = it.reader('input_files/Schroedinger4.inp')
START4 = it.getxmin(DATALINES4)
STOP4 = it.getxmax(DATALINES4)
N4 = it.getnumofpoints(DATALINES4)-1
X4 = np.linspace(START4, STOP4, N4+1)
INTTYPE4 = it.interpolationtype(DATALINES4) #type of interpolation
A4 = it.getA(DATALINES4)
VX4 = np.asarray_chkfinite(it.getxvalues(DATALINES4), dtype=np.float64, order='C')
VY4 = np.asarray_chkfinite(it.getyvalues(DATALINES4), dtype=np.float64, order='C')
FVALUE4 = it.getfirsteigen(DATALINES4)-1
LVALUE4 = it.getlasteigen(DATALINES4)-1
NUMEV4 = LVALUE4-FVALUE4
AA4 = it.eigen(VX4, VY4, X4, INTTYPE4, FVALUE4, LVALUE4, A4, N4)
EIVAL4 = AA4[0]
so.saveeigenvaluestest(EIVAL4, FVALUE4, LVALUE4, 'testfiles/energietest4.dat')
so.savepotentialtest(slv.potential(VX4, VY4, X4, INTTYPE4), X4, 'testfiles/potentialtest4.dat')
def test_potential():
    """The funtion tests the potential
    """
    refpot4 = di.readcalcpotential('reference_files/potential4.dat')
    pot4 = di.readcalcpotential('testfiles/potentialtest4.dat')
    assert np.all(pot4-refpot4 < 0.01)

def test_energies():
    """The function tests the energies
    """
    refenergies4 = di.readcalceigenval('reference_files/energies4.dat')
    energies4 = di.readcalceigenval('testfiles/energietest4.dat')
    assert np.all(refenergies4-energies4 < 0.01)