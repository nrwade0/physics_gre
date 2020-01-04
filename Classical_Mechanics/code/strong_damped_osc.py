#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 02:04:07 2019

@author: nick
"""


import numpy as np
import pylab as py

t = np.linspace(0, 11, 250)


omega0= 1
beta = 1.9

temp = np.sqrt(beta**2 - omega0**2)

x1 = np.exp(-t*(beta - temp))
x2 = np.exp(-t*(beta + temp))

C1 = 1
C2 = -1

x = C1*x1 + C2*x2


py.figure(1)
py.title('Strong damping oscillations')
py.xlabel('t')
py.ylabel('x')
py.xticks([])
py.yticks([])
py.plot(t, x, 'g')
py.axhline(y=0, color='k')
py.axvline(x=0, color='k')
py.show()