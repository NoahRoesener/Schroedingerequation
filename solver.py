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
H = 4.0/N
A = 1/(M*H**2)


def Eigen(Vx, Vy, x, inttype, fvalue, lvalue):
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(Vx, Vy, x, method=inttype)
    elif inttype == 'polynomial':
        coefficients = np.polyfit(Vx, Vy, 2)
        grid = np.polyval(coefficients, x)
    d = grid+A
    e = np.zeros(N)+(-0.5)*A
    eev = sclin.eigh_tridiagonal(d, e, select='i', select_range=(fvalue, lvalue))
    return eev


def Potential(Vx, Vy, x, inttype):
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(Vx, Vy, x, method=inttype)
        return grid
    elif inttype == 'polynomial':
        coefficients = np.polyfit(Vx, Vy, 2)
        grid = np.polyval(coefficients, x)
        return grid

def normalize(dd):
    norm = np.linalg.norm(dd)
    if norm == 0:
        return dd
    else:
        return dd / norm

def Erwartung(vec, numev, x):
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        Erwvec = nvec*nvec*x
        sum = 0
        for qq in Erwvec:
            sum += qq
        ll.append(sum*H)
        ii += 1
    return ll


def Erwartungquadrat(vec, numev, x):
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        Erwvec = nvec*nvec*x*x
        sum = 0
        for qq in Erwvec:
            sum += qq
        ll.append(sum*H)
        ii += 1
    return ll