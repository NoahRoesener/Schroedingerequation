#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:31:10 2018

@author: eikegroen
"""
import numpy as np 
import scipy.linalg as sclin
from scipy.interpolate import griddata
start = -2
stop = 2 #Intervall 
M = 2.0 #mass of the Objekt 
n = 1998 
h = 4.0/n
inttype = 'linear' #type of interpolation
a = 1/(M*h**2)
x = np.linspace(start,stop,n+1)
Vx = np.array([-2.0,2.0])
Vy = np.array([0.0,0.0])
fvalue=0
lvalue=0
def Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n):
    grid=griddata(Vx,Vy,x,method=inttype)
    d=grid+a
    e=np.zeros(n)+(-0.5)*a
    eev=sclin.eigh_tridiagonal(d,e,select='i',select_range=(fvalue,lvalue))
    return eev
aa=Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n)
ev=aa[0]
evec=aa[1]
print(ev)
import matplotlib.pyplot as plt
plt.plot(x,evec)
plt.show()




        
        

    




