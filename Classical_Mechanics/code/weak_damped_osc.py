#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 01:59:34 2019

@author: nick
"""

import numpy as np
import pylab as py

t = np.linspace(0, 29.75, 250)

Ax = 1
omega1 = 1
beta = 0.10

delta = 0

x = Ax * np.exp(-beta*t)*np.cos(omega1*t-delta)


py.figure(1)
py.title('Weak damping oscillations')
py.xlabel('t')
py.ylabel('x')
py.xticks([])
py.yticks([])
py.plot(t, x, 'g')
py.axhline(y=0, color='k')
py.axvline(x=0, color='k')
py.show()