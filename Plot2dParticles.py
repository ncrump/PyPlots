"""
Created on Sat Apr 04 18:21:52 2015
Reads particle file and plots positions and velocities
"""

import numpy as np
import matplotlib.pyplot as plt

# read data files
px,py,vx,vy = np.loadtxt('particles.txt',dtype=float,unpack=True)

# set parameters
xymin = -4.1  # lower plot limit
xymax =  4.1  # upper plot limit
dy    =  2.0  # y-axis step size
cfl   =  1.0  # CFL number

# compute allowable timestep
vmax = max((vx**2 + vy**2)**0.5)
dt = cfl*(dy/vmax)
print '\ndt =',dt

# get normalization
mag = (vx**2 + vy**2)**0.5
gxnorm = vx/mag
gynorm = vy/mag

# make plots
plt.figure()
plt.plot(px,py,'bo')
plt.xlim(xymin,xymax)
plt.ylim(xymin,xymax)
Q = plt.quiver(px,py,vx,vy,mag)
plt.title('2D Random Particles')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()