# -*- coding: utf-8 -*-
"""
3/31/19
nrwade0
Pendulum or skateboarder on a halfpipe example
"""

# Links using odeint on scipy
# http://sam-dolan.staff.shef.ac.uk/mas212/notebooks/ODE_Example.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html

import numpy as np
import matplotlib.pyplot as py
from scipy.integrate import odeint

# Equation is $ \ddot \phi = -\frac{g}{R}sin\phi $

# Constants
g = 9.81 # m/s^2
R = 5    # m

def dphi_dt(phi, t):
    # phi[0] = phi position ... phi[1] = phi velocity
    return [phi[1], -g/R * np.sin(phi[0])]

# Initial value vector, \phi_0 = 2 meters up, \dot \phi_0 = 0 from rest 
phi = [2, 0]

# Span of time 0 to 20 seconds
t = np.linspace(0,20,10000)

phit = odeint(dphi_dt, phi, t)

py.xlabel("t")
py.ylabel("y")
py.title("Pendulum")
py.plot(t, phit[:,0],'b-')
