#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:19:10 2018

@author: eikegroen
"""

import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(-1,10,100)
y1=np.sin(x1)
y2=x1
x2=np.cos(x1)
plt.figure()
plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.show
plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.plot(x2,y1)
plt.show()
