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
import saveoutput as so

M = di.getmass() #mass of the object
N = di.getnumofpoints()-1
if di.getxmin() < 0:
    H = (abs(di.getxmin())+abs(di.getxmax()))/N
else:
    H = (di.getxmax()-di.getxmin())/N
A = 1/(M*H**2)


def eigen(vx, vy, xx, inttype, fvalue, lvalue):
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
    if inttype == 'cubic' or inttype == 'linear':
        grid = griddata(vx, vy, xx, method=inttype)
        return grid
    elif inttype == 'polynomial':
        coefficients = np.polyfit(vx, vy, 2)
        grid = np.polyval(coefficients, xx)
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


def erwartung(vec, numev, xx):
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        Erwvec = nvec*nvec*xx
        su = 0
        for qq in Erwvec:
            su += qq
        ll.append(su*H)
        ii += 1
    return ll


def erwartungquadrat(vec, numev, xx):
    ii = 0
    ll = []
    while ii <= numev:
        bvec = vec[:, ii]
        nvec = normalize(bvec)
        Erwvec = nvec*nvec*xx*xx
        su = 0
        for qq in Erwvec:
            su += qq
        ll.append(su*H)
        ii += 1
    return ll

def unschaerfe(erw, erwq):
     uns = np.sqrt(np.array(erwq)-np.array(erw)*np.array(erw))
     return(uns)
