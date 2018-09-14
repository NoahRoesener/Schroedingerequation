#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 25:22:44 2028

@author: eikegroen
"""

import datainput as di
import solver as slv
import saveoutput as so
import numpy as np
import inputtests as it
DATALINES2 = it.reader('input_files/Schroedinger2.inp')
START2 = it.getxmin(DATALINES2)
STOP2 = it.getxmax(DATALINES2)
N2 = it.getnumofpoints(DATALINES2)-1
X2 = np.linspace(START2, STOP2, N2+1)
INTTYPE2 = it.interpolationtype(DATALINES2) #type of interpolation
A2 = it.getA(DATALINES2)
VX2 = np.asarray_chkfinite(it.getxvalues(DATALINES2), dtype=np.float64, order='C')
VY2 = np.asarray_chkfinite(it.getyvalues(DATALINES2), dtype=np.float64, order='C')
FVALUE2 = it.getfirsteigen(DATALINES2)-1
LVALUE2 = it.getlasteigen(DATALINES2)-1
NUMEV2 = LVALUE2-FVALUE2
AA2 = it.eigen(VX2, VY2, X2, INTTYPE2, FVALUE2, LVALUE2, A2, N2)
EIVAL2 = AA2[0]
so.saveeigenvaluestest(EIVAL2, FVALUE2, LVALUE2, 'testfiles/energietest2.dat')
so.savepotentialtest(slv.potential(VX2, VY2, X2, INTTYPE2), X2, 'testfiles/potentialtest2.dat')
def test_potential():
    """The function tests the potentials
    """
    refpot2 = di.readcalcpotential('reference_files/potential2.dat')
    pot2 = di.readcalcpotential('testfiles/potentialtest2.dat')
    assert np.all(pot2-refpot2 < 0.01)

def test_energies():
    """The function tests the energies
    """
    refenergies2 = di.readcalceigenval('reference_files/energies2.dat')
    energies2 = di.readcalceigenval('testfiles/energietest2.dat')
    assert np.all(refenergies2-energies2 < 0.1)
