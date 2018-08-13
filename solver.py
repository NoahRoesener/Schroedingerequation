#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:31:10 2018

@author: eikegroen
"""
import numpy as np 
import DataInput
from scipy import linalg as sclin
from scipy.linalg import eigh_tridiagonal
from scipy.interpolate import griddata
import DataInput as di
start = getXMin()
stop = getXMax() 
M = getMass() #mass of the object 
n = getNumOfPoints()-1 
h = 4.0/n
inttype = interpolationType() #type of interpolation
a = 1/(M*h**2)
x = np.linspace(stop,start,n+1)
Vx = np.array([-2.0,2.0])
Vy = np.array([0.0,0.0])
fvalue=2
lvalue=2
nev=lvalue-fvalue 
def Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n):
    if inttype == 'cubic' or 'linear':
        grid=griddata(Vx,Vy,x,method=inttype)
    elif inttype == 'polynomial':
        coefficients=np.polyfit(Vx,Vy,2)
        grid=np.polyval(coefficients,x)
 d=grid+a
 e=np.zeros(n)+(-0.5)*a
 eev=sclin.eigh_tridiagonal(d,e,select='i',select_range=(fvalue,lvalue))
 return eev
aa=Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n)
ev=aa[0]
evec=aa[1]
print(evec)
def normalize(evec):
    norm = np.linalg.norm(evec)
    if norm == 0: 
       return evec
    else:
        return evec / norm 
nevec=normalize(evec)
print(nevec)
import matplotlib.pyplot as plt
plt.plot(x,nevec)





        
        

    




