#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 00:06:35 2019

@author: nick
"""

import numpy as np
import pylab as py

t = np.linspace(0, 30, 250)

Ax = 1
Ay = 1
omega = 1

delta = np.pi/4

x = Ax*np.cos(omega*t)
y = Ay*np.cos(omega*t - delta)


py.figure(1)
py.title('delta = pi/4')
py.xlabel('x')
py.ylabel('y')
py.xticks([])
py.yticks([])
py.plot(x, y)
py.axhline(y=0, color='k')
py.axvline(x=0, color='k')
py.show()