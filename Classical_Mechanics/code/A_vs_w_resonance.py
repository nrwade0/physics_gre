#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:51:59 2019

@author: nick
"""

import numpy as np
import pylab as py

def f(x):
    return (ff*ff)/((omega0**2 - omega**2)**2 + 4*beta**2*omega**2)

ff = 1
omega0 = np.linspace(0,8,300)
omega = 2
beta = 0.1*omega

py.figure(1)
py.plot(omega0, f(omega0), 'k-')
py.title('Resonance at omega = 2')
py.xlabel('omega')
py.ylabel('A^2')
#py.xticks([])
py.yticks([])
py.show()