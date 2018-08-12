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
start = -20
stop = 20 #Intervall 
M = float(getMass()) #mass of the object 
n = 1998 
h = 40.0/n
inttype = 'linear' #type of interpolation
a = 1/(M*h**2)
x = np.linspace(start,stop,n+1)
Vx = np.array([-20.0,-10.0,0.0,10.0,20.0])
Vy = np.array([35.0,0.0,2.0,0.0,35.0])
fvalue=2
lvalue=2
nev=lvalue-fvalue 
def Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n):
    grid=griddata(Vx,Vy,x,method=inttype)
    d=grid+a
    e=np.zeros(n)+(-0.5)*a
    eev=sclin.eigh_tridiagonal(d,e,select='i',select_range=(fvalue,lvalue))
    return eev
    
aa=Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n)
ev=aa[0]
evec=aa[1]

import matplotlib.pyplot as plt
plt.plot(x,evec)





        
        

    




