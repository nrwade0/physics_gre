#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 00:56:28 2019

@author: nick
"""

import numpy as np
import pylab as py


def drive(t):
    return A*np.cos(omega*t - delta)

def x(t):
    return A*np.cos(omega*t - delta) + np.exp(-beta*t)*(B1*np.cos(omega1*t) + B2*np.sin(omega1*t))
    

# constants
A = 1.06
B1 = -1.05
B2 = -0.0572
omega = 2*np.pi
omega1 = 9.987*np.pi
delta = 0.0208
beta = 5*omega/20

t = np.linspace(0,5,300)
x = x(t)
drive = drive(t)

py.figure(1)
py.plot(t,x,'r')
py.axhline(y=0, color='k')
py.axvline(x=0, color='k')
py.title('Driven Damped Oscillator')
py.xlabel('t')
py.ylabel('x(t)')
py.ylim(-2,2)
py.xticks([])
py.yticks([])


py.figure(2)
py.plot(t,drive,'b')
py.axhline(y=0, color='k')
py.axvline(x=0, color='k')
py.title('Sinusoidal Driving Force')
py.xlabel('t')
py.ylabel('f(t)')
py.ylim(-2,2)
py.xticks([])
py.yticks([])


py.show()