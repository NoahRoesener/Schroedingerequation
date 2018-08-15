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
import matplotlib.pyplot as plt
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
fvalue=0
lvalue=4
numev=lvalue-fvalue 
def Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n):
    if inttype == 'cubic' or inttype=='linear':
        grid=griddata(Vx,Vy,x,method=inttype)
    elif inttype == 'polynomial':
        coefficients=np.polyfit(Vx,Vy,2)
        grid=np.polyval(coefficients,x)
<<<<<<< HEAD
 #d=1+a
 #e=np.zeros(n)+(-0.5)*a
 eev=sclin.eigh_tridiagonal(d,e,select='i',select_range=(fvalue,lvalue))
 return eev
=======
    d=grid+a
    e=np.zeros(n)+(-0.5)*a
    eev=sclin.eigh_tridiagonal(d,e,select='i',select_range=(fvalue,lvalue))
    return eev
>>>>>>> 340a0152db8f138807a0432733237d8551a10f26
aa=Eigen(Vx,Vy,x,inttype,fvalue,lvalue,n)
ev=aa[0]
evec=aa[1]
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
Erwq=Erwartungquadrat(evec)
Erw=Erwartung(evec)
Unschärfe=np.sqrt(np.array(Erwq)-np.array(Erw)*np.array(Erw))
print(Unschärfe)
plt.plot(np.array(Erw),ev,'x',color='blue')
ii=0
while ii <= numev:
    vec=evec[:,ii]
    nvec=normalize(vec)
    nvec=7*nvec+ev[ii]
    plt.plot(x,nvec)
    plt.plot(x,np.zeros(n+1)+ev[ii],color='grey')
    ii+=1







        
        

    




