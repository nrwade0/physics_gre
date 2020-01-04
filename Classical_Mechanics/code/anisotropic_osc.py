#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 00:16:27 2019

@author: nick
"""

import numpy as np
import pylab as py

t = np.linspace(0, 24, 250)

Ax = 1
Ay = 1
omegax = np.sqrt(2)
omegay = 1

delta = np.pi/2

x = Ax*np.cos(omegax*t)
y = Ay*np.cos(omegay*t - delta)


py.figure(1)
py.title('Quasiperiodic Motion')
py.xlabel('x')
py.ylabel('y')
py.xticks([])
py.yticks([])
py.plot(x, y)
py.axhline(y=0, color='k')
py.axvline(x=0, color='k')
py.show()