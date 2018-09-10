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
import matplotlib.pyplot as plt
import saveOutput as so

M = di.getMass() #mass of the object 
n = di.getNumOfPoints()-1 
h = 4.0/n
a = 1/(M*h**2)


def Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n):
    if inttype == 'cubic' or inttype=='linear':
        grid=griddata(Vx,Vy,x, method= inttype)
    elif inttype == 'polynomial':
        coefficients=np.polyfit(Vx,Vy,2)
        grid=np.polyval(coefficients,x)
    d=grid+a
    e=np.zeros(n)+(-0.5)*a
    eev=sclin.eigh_tridiagonal(d,e,select='i',select_range=(fvalue,lvalue))
    return eev


def Potential(Vx,Vy,x,inttype,fvalue,lvalue,n):
    if inttype == 'cubic' or inttype=='linear':
        grid=griddata(Vx,Vy,x,method=inttype)
        return grid
    elif inttype == 'polynomial':
        coefficients=np.polyfit(Vx,Vy,2)
        grid=np.polyval(coefficients,x)
        return grid



def normalize(dd):
    norm = np.linalg.norm(dd)
    if norm == 0: 
       return dd
    else:
        return dd / norm
    
    
def Erwartung(vec, numev, x):
    ii=0
    ll=[]
    while ii <= numev:
        bvec=vec[:,ii]
        nvec=normalize(bvec)
        Erwvec=bvec*bvec*x
        sum=0
        for qq in Erwvec:
            sum+=qq
        ll.append(sum*h)
        ii+=1
    return ll


def Erwartungquadrat(vec, numev, x):
    ii=0
    ll=[]
    while ii <= numev:
        bvec=vec[:,ii]
        nvec=normalize(bvec)
        Erwvec=bvec*bvec*x*x
        sum=0
        for qq in Erwvec:
            sum+=qq
        ll.append(sum*h)
        ii+=1
    return ll














        
        

    




