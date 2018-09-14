#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:31:10 2018

@author: eikegroen
"""
import numpy as np
from scipy import linalg as sclin
from scipy.linalg import eigh_tridiagonal
from scipy.interpolate import griddata
import DataInput as di

M = di.getmass() #mass of the object
N = di.getnumofpoints()-1
if di.getxmin() < 0:
    H = (abs(di.getxmin())+abs(di.getxmax()))/N
else:
    H = (di.getxmax()-di.getxmin())/N
A = 1/(M*H**2)


def eigen(vx, vy, xx, inttype, fvalue, lvalue):
    """The function is calculating the eigenvalues and and eigenvectors.

    :type Vx: [float]
    :param Vx: x-values of the interpolation points

    :type Vy: [float]
    :param Vy: y-values of the interpolation points

    :type x: np.array(float)
    :param x: x-values

    :type inttype: string
    :param inttype: type of interpolation

    :type fvalue: int
    :param fvalue: first eigenvalue to be calculated

    :type lvalue: int
    :param lvalue: last eigenvalue to be calculated

    :rtype: (np.array(float),np.array(float))
    :returns: Returns a tuple with the the eigenvalues and and eigenvectors
    """
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(vx, vy, xx, method=inttype)
    elif inttype == 'polynomial':
        coefficients = np.polyfit(vx, vy, 2)
        grid = np.polyval(coefficients, xx)
    d = grid+A
    e = np.zeros(N)+(-0.5)*A
    eiva, eive = sclin.eigh_tridiagonal(d, e, select_range=(fvalue, lvalue))
    return eiva, eive


def potential(vx, vy, xx, inttype):
    """The function is calculating the potential.

    :type Vx: [float]
    :param Vx: x-values of the interpolation points

    :type Vy: [float]
    :param Vy: y-values of the interpolation points

    :type x: np.array(float)
    :param x: x-values

    :type inttype: string
    :param inttype: type of interpolation

    :rtype: np.array(float)
    :returns: Returns a np.array with the y-values of the potential
    """
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(vx, vy, xx, method=inttype)
        return grid
    elif inttype == 'polynomial':
        coefficients = np.polyfit(vx, vy, 2)
        grid = np.polyval(coefficients, xx)
        return grid

def normalize(dd):
    """The function normalizes vectors.

    :type dd: np.array(float)
    :param dd: Vector

    :rtype: np.array(float)
    :returns: Returns the normalized vector
    """
    norm = 0
    for element in dd:
        norm = norm+element**2
    norm = norm*H
    if norm == 0:
        return dd
    else:
        return dd/norm


def erwartung(vec, numev, xx):
    """
    The function is calculating the erwartungswert.

    :type vec: np.array(float)
    :param vec: np.array with eigenvectors

    :type numev: float
    :param numev: Number of eigenvectors

    :type x: np.array(float)
    :param x: x-values
    :rtype: np.array(float)
    :returns: Returns a np.array with expected values
    """
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        erwvec = nvec*nvec*xx
        su = 0
        for qq in erwvec:
            su += qq
        ll.append(su*H)
        ii += 1
    return ll


def erwartungquadrat(vec, numev, xx):
    """
    The function is calculating the erwartungsquadrat.

    :type vec: np.array(float)
    :param vec: np.array with eigenvectors

    :type numev: float
    :param numev: Number of eigenvectors

    :type x: np.array(float)
    :param x: x-values
    :rtype: np.array(float)
    :returns: Returns a np.array with the squared expected values
    """
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        erwvec = nvec*nvec*xx*xx
        su = 0
        for qq in erwvec:
            su += qq
        ll.append(su*H)
        ii += 1
    return ll

def unschaerfe(erw, erwq):
    """The function calculates the unschaerfe

    ARGS:
        erw: The container where the erwartungwerte are stored in an array.
        erwq: The array where the squared erwartungswerte are stored in.

    RETURN:
         Returns the unschaerfe as an array.
    """
    uns = np.sqrt(np.array(erwq)-np.array(erw)*np.array(erw))
    return uns
