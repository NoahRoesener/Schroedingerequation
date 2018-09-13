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
import saveOutput as so

M = di.getMass() #mass of the object
N = di.getNumOfPoints()-1
if di.getXMin()<0:
    H = (abs(di.getXMin())+abs(di.getXMax()))/N
else:
    H = (di.getXMax()-di.getXMin())/N
A = 1/(M*H**2)


def Eigen(Vx, Vy, x, inttype, fvalue, lvalue):
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(Vx, Vy, x, method=inttype)
    elif inttype == 'polynomial':
        coefficients = np.polyfit(Vx, Vy, 2)
        grid = np.polyval(coefficients, x)
    d = grid+A
    e = np.zeros(N)+(-0.5)*A
    eiva, eive = sclin.eigh_tridiagonal(d, e, select_range=(fvalue, lvalue))
    return eiva, eive


def Potential(Vx, Vy, x, inttype):
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(Vx, Vy, x, method=inttype)
        return grid
    elif inttype == 'polynomial':
        coefficients = np.polyfit(Vx, Vy, 2)
        grid = np.polyval(coefficients, x)
        return grid

def normalize(dd):
     norm = 0
     for element in dd:
          norm = norm+element**2
     norm = norm*H
     if norm == 0:
          return dd
     else:
          return dd/norm


def Erwartung(vec, numev, x):
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        Erwvec = nvec*nvec*x
        su = 0
        for qq in Erwvec:
            su += qq
        ll.append(su*H)
        ii += 1
    return ll


def Erwartungquadrat(vec, numev, x):
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        Erwvec = nvec*nvec*x*x
        su = 0
        for qq in Erwvec:
            su += qq
        ll.append(su*H)
        ii += 1
    return ll