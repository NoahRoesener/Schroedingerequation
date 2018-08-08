#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:31:10 2018

@author: eikegroen
"""
import numpy as np 
import scipy as sc
from scipy.linalg import eigh_tridiagonal
from scipy.interpolate import griddata
start = -2
stop = 2
M = 2.0
n = 10
h = 4.0/n
inttype = 'linear'
a = 1/(M*h*h)
dx = np.linspace(start,stop,n+1)
Vx = np.array([-2.0,2.0])
Vy = np.array([0.0,0.0])
grid=griddata(Vx,Vy,dx,method=inttype)
fvalue=1
lvalue=7
d=grid+a
e=np.zeros(n)+(-0.5)*a
ev=eigh_tridiagonal(d,e,select='a')
print(ev)





        
        

    




