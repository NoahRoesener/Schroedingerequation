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
start = di.getXMin()
stop = di.getXMax() 
M = di.getMass() #mass of the object 
n = di.getNumOfPoints()-1 
h = 4.0/n
x=np.linspace(stop, start, n+1)
inttype = di.interpolationType() #type of interpolation
a = 1/(M*h**2)
Vx =np.asarray_chkfinite(di.getXValues(), dtype=np.float64, order='C')
Vy = np.asarray_chkfinite(di.getYValues(), dtype=np.float64, order='C')
fvalue=di.getFirstEigen()-1
lvalue=di.getLastEigen()-1
numev=lvalue-fvalue 


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
    
    
def Erwartung(vec):
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


def Erwartungquadrat(vec):
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


aa=Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n)
ev=aa[0]
evec=aa[1]
Pot=Potential(Vx,Vy,x,inttype,fvalue,lvalue,n)
Erwq=Erwartungquadrat(evec)
Erw=Erwartung(evec)
Unschärfe=np.sqrt(np.array(Erwq)-np.array(Erw)*np.array(Erw))


a=so.saveWavefunc(evec, x)












        
        

    




