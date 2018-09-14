#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:17:51 2018

@author: eikegroen
"""

import datainput as di
import solver as slv
import saveoutput as so
import numpy as np
import inputtests as it
DATALINES5 = it.reader('input_files/Schroedinger5.inp')
START5 = it.getxmin(DATALINES5)
STOP5 = it.getxmax(DATALINES5)
N5 = it.getnumofpoints(DATALINES5)-1
X5 = np.linspace(START5, STOP5, N5+1)
INTTYPE5 = it.interpolationtype(DATALINES5) #type of interpolation
A5 = it.getA(DATALINES5)
VX5 = np.asarray_chkfinite(it.getxvalues(DATALINES5), dtype=np.float64, order='C')
VY5 = np.asarray_chkfinite(it.getyvalues(DATALINES5), dtype=np.float64, order='C')
FVALUE5 = it.getfirsteigen(DATALINES5)-1
LVALUE5 = it.getlasteigen(DATALINES5)-1
NUMEV5 = LVALUE5-FVALUE5
AA5 = it.eigen(VX5, VY5, X5, INTTYPE5, FVALUE5, LVALUE5, A5, N5)
EIVAL5 = AA5[0]
so.saveeigenvaluestest(EIVAL5, FVALUE5, LVALUE5, 'testfiles/energietest5.dat')
so.savepotentialtest(slv.potential(VX5, VY5, X5, INTTYPE5), X5, 'testfiles/potentialtest5.dat')
def test_potential():
    """The funtion tests the potential
    """
    refpot5 = di.readcalcpotential('reference_files/potential5.dat')
    pot5 = di.readcalcpotential('testfiles/potentialtest5.dat')
    assert np.all(pot5-refpot5 < 0.01)

def test_energies():
    """The function tests the energies
    """
    refenergies5 = di.readcalceigenval('reference_files/energies5.dat')
    energies5 = di.readcalceigenval('testfiles/energietest5.dat')
    assert np.all(refenergies5-energies5 < 0.01)