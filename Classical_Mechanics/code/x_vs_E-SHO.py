#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:57:11 2019

@author: nick
"""

import numpy as np
import pylab as py


x = np.linspace(-5,5,100)
y = .5*1*x*x


py.figure(1)

# create axes
py.axhline(y=0, color='k')
py.axvline(x=0, color='k')

# plot parabola
py.plot(x,y)

# remove tick values
#py.xticks([])
#py.yticks([])

#add amplitude lines
py.axhline(y=4, xmin=0.25, xmax=0.75, color='g')
py.axvline(x=-8**.5, ymin=0.05, ymax=0.33, color='r')
py.axvline(x=8**.5, ymin=0.05, ymax=0.33, color='r')

#add text
py.text(s='A', x=8**0.5, y=-0.5, color='r', fontsize=12)
py.text(s='-A', x=-8**0.5, y=-0.5, color = 'r', fontsize=12)
py.text(s='E', x=8**0.5+0.15, y=4, color='g', fontsize=12)

#add labels
py.xlabel('x (distance)')
py.ylabel('U(x) (energy)')
py.title('Simple Harmonic Oscillator')


py.show()
