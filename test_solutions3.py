#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:29:27 2018

@author: eikegroen
"""

import datainput as di
import solver as slv
import saveoutput as so
import numpy as np
import inputtests as it
DATALINES3 = it.reader('input_files/Schroedinger3.inp')
START3 = it.getxmin(DATALINES3)
STOP3 = it.getxmax(DATALINES3)
N3 = it.getnumofpoints(DATALINES3)-1
X3 = np.linspace(START3, STOP3, N3+1)
INTTYPE3 = it.interpolationtype(DATALINES3) #type of interpolation
A3 = it.getA(DATALINES3)
VX3 = np.asarray_chkfinite(it.getxvalues(DATALINES3), dtype=np.float64, order='C')
VY3 = np.asarray_chkfinite(it.getyvalues(DATALINES3), dtype=np.float64, order='C')
FVALUE3 = it.getfirsteigen(DATALINES3)-1
LVALUE3 = it.getlasteigen(DATALINES3)-1
NUMEV3 = LVALUE3-FVALUE3
AA3 = it.eigen(VX3, VY3, X3, INTTYPE3, FVALUE3, LVALUE3, A3, N3)
EIVAL3 = AA3[0]
so.saveeigenvaluestest(EIVAL3, FVALUE3, LVALUE3, 'testfiles/energietest3.dat')
so.savepotentialtest(slv.potential(VX3, VY3, X3, INTTYPE3), X3, 'testfiles/potentialtest3.dat')
def test_potential():
    """The funtion tests the potential
    """
    refpot3 = di.readcalcpotential('reference_files/potential3.dat')
    pot3 = di.readcalcpotential('testfiles/potentialtest3.dat')
    assert np.all(pot3-refpot3 < 0.01)

def test_energies():
    """The function tests the energies
    """
    refenergies3 = di.readcalceigenval('reference_files/energies3.dat')
    energies3 = di.readcalceigenval('testfiles/energietest3.dat')
    assert np.all(refenergies3-energies3 < 0.01)